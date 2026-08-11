import argparse
import csv
import json
import time
from pathlib import Path

from dotenv import load_dotenv

from backend.config import ANSWER_MODELS
from backend.generate import generate_answer, generate_raw, is_configured
from backend import vectorstore

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
BENCHMARK_DIR = BASE_DIR / "data" / "benchmark"
RESULTS_DIR = BENCHMARK_DIR / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def load_benchmark(jsonl_path: Path) -> list[dict]:
    with open(jsonl_path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def _get_qtext(q: dict) -> str:
    return q.get("question_text") or q.get("prompt") or q.get("question") or ""


def evaluate_base_llm(questions: list[dict], model_label: str) -> list[dict]:
    if not is_configured(model_label):
        spec = ANSWER_MODELS[model_label]
        raise ValueError(f"Missing API key: set {spec['api_key_env']} in your environment for {model_label}")

    results = []
    print(f"\n--- Running Base LLM Evaluation for: {model_label} ({len(questions)} questions) ---")
    for i, q in enumerate(questions, 1):
        qtext = _get_qtext(q)
        print(f"[{i}/{len(questions)}] Processing {q['question_id']} (Tier {q['tier']})...", end="", flush=True)
        t0 = time.perf_counter()
        try:
            resp = generate_raw(qtext, model_label)
            elapsed = time.perf_counter() - t0
            print(f" Done ({elapsed:.2f}s)")
        except Exception as e:
            resp = f"ERROR: {str(e)}"
            print(f" Failed ({str(e)})")
        
        results.append({
            "question_id": q.get("question_id"),
            "tier": q.get("tier"),
            "question_text": qtext,
            "expected_answer": q.get("expected_answer"),
            "source_citation": q.get("source_citation"),
            "source_url": q.get("source_url"),
            "known_trap": q.get("known_trap"),
            "model": model_label,
            "response": resp
        })
        time.sleep(0.2)
    return results


def evaluate_rag_system(questions: list[dict], embedding_model_label: str, answer_model_label: str, top_k: int = 4, hybrid_weight: float = 0.5) -> list[dict]:
    if not is_configured(answer_model_label):
        spec = ANSWER_MODELS[answer_model_label]
        raise ValueError(f"Missing API key: set {spec['api_key_env']} in your environment for {answer_model_label}")

    results = []
    print(f"\n--- Running RAG Evaluation ({embedding_model_label} + {answer_model_label}) ({len(questions)} questions) ---")
    for i, q in enumerate(questions, 1):
        qtext = _get_qtext(q)
        print(f"[{i}/{len(questions)}] RAG Query {q['question_id']} (Tier {q['tier']})...", end="", flush=True)
        t0 = time.perf_counter()
        try:
            chunks = vectorstore.query(embedding_model_label, qtext, top_k=top_k, hybrid_weight=hybrid_weight)
            chunk_texts = [c["text"] for c in chunks]
            if chunk_texts:
                resp = generate_answer(qtext, chunk_texts, answer_model_label)
            else:
                resp = "RAG Notice: No relevant documents found in knowledge base."
            elapsed = time.perf_counter() - t0
            print(f" Done ({elapsed:.2f}s)")
        except Exception as e:
            resp = f"ERROR: {str(e)}"
            chunks = []
            print(f" Failed ({str(e)})")

        results.append({
            "question_id": q.get("question_id"),
            "tier": q.get("tier"),
            "question_text": qtext,
            "expected_answer": q.get("expected_answer"),
            "source_citation": q.get("source_citation"),
            "source_url": q.get("source_url"),
            "known_trap": q.get("known_trap"),
            "model": f"RAG ({answer_model_label})",
            "response": resp,
            "num_retrieved_chunks": len(chunks)
        })
        time.sleep(0.2)
    return results


def save_evaluation_results(results: list[dict], output_name: str):
    json_path = RESULTS_DIR / f"{output_name}.json"
    csv_path = RESULTS_DIR / f"{output_name}.csv"

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    if results:
        fieldnames = list(results[0].keys())
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            for r in results:
                writer.writerow(r)

    print(f"Saved evaluation output to:\n  - {json_path}\n  - {csv_path}")


def main():
    parser = argparse.ArgumentParser(description="Evaluate SEBI Benchmark across Base LLMs or RAG")
    parser.add_argument("--mode", choices=["base", "rag", "all_base"], default="all_base", help="Evaluation mode")
    parser.add_argument("--model", choices=list(ANSWER_MODELS), help="Specific model for base evaluation")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of questions to evaluate (for testing)")
    args = parser.parse_args()

    input_file = BENCHMARK_DIR / "sebi_benchmark_50.jsonl"
    if not input_file.exists():
        raise FileNotFoundError("sebi_benchmark_50.jsonl not found. Run scripts/build_sebi_benchmark.py first.")

    questions = load_benchmark(input_file)
    if args.limit:
        questions = questions[:args.limit]

    if args.mode == "all_base":
        for model_label in ANSWER_MODELS:
            output_name = f"base_{model_label.split()[0].lower().replace('-', '_')}"
            results = evaluate_base_llm(questions, model_label)
            save_evaluation_results(results, output_name)
    elif args.mode == "base" and args.model:
        output_name = f"base_{args.model.split()[0].lower().replace('-', '_')}"
        results = evaluate_base_llm(questions, args.model)
        save_evaluation_results(results, output_name)
    elif args.mode == "rag":
        model_label = args.model or "gpt-5-nano (OpenAI)"
        output_name = "rag_evaluation_results"
        results = evaluate_rag_system(questions, "MiniLM-L6 (fast, 384d)", model_label)
        save_evaluation_results(results, output_name)


if __name__ == "__main__":
    main()
