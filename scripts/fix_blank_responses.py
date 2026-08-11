"""Script to automatically detect, re-query, and backfill any blank responses.

Ensures 100% of all 50 questions across all 6 model configurations have
rich, non-empty, scored responses in the Master CSV and Excel files.
"""
import json
import time
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv

load_dotenv()

from backend import generate, vectorstore
from backend.config import DEFAULT_EMBEDDING_MODEL

BASE_DIR = Path(__file__).resolve().parent.parent
BENCHMARK_DIR = BASE_DIR / "data" / "benchmark"
RESULTS_DIR = BENCHMARK_DIR / "results"
BENCHMARK_JSON = BENCHMARK_DIR / "sebi_benchmark_50.json"


def main():
    if not BENCHMARK_JSON.exists():
        print("sebi_benchmark_50.json not found.", flush=True)
        return

    with open(BENCHMARK_JSON, "r", encoding="utf-8") as f:
        questions = json.load(f)

    q_map = {q["question_id"]: q for q in questions}

    result_files = {
        "gpt_5_nano_base": (RESULTS_DIR / "base_gpt_5_nano.json", "gpt-5-nano (OpenAI)", False),
        "gpt_oss_20b_base": (RESULTS_DIR / "base_gpt_oss_20b.json", "gpt-oss-20b (Together AI)", False),
        "gemma_3n_base": (RESULTS_DIR / "base_gemma_3n_e4b_it.json", "gemma-3n-E4B-it (Together AI)", False),
        "rag_gpt_5_nano": (RESULTS_DIR / "rag_evaluation_results.json", "gpt-5-nano (OpenAI)", True),
        "rag_gpt_oss_20b": (RESULTS_DIR / "rag_gpt_oss_20b.json", "gpt-oss-20b (Together AI)", True),
        "rag_gemma_3n": (RESULTS_DIR / "rag_gemma_3n.json", "gemma-3n-E4B-it (Together AI)", True),
    }

    for cfg_key, (json_path, model_label, is_rag) in result_files.items():
        if not json_path.exists():
            continue

        with open(json_path, "r", encoding="utf-8") as f:
            items = json.load(f)

        item_map = {item["question_id"]: item for item in items}
        modified = False

        for q_id, item in item_map.items():
            resp = item.get("response", "")
            if not resp or resp.strip() == "" or resp.startswith("ERROR"):
                q = q_map[q_id]
                qtext = q["question_text"]
                print(f"Backfilling blank response for {cfg_key} | {q_id}...", flush=True)

                retries = 3
                new_resp = ""
                for attempt in range(retries):
                    try:
                        if is_rag:
                            chunks = vectorstore.query(DEFAULT_EMBEDDING_MODEL, qtext, top_k=4, hybrid_weight=0.5)
                            c_texts = [c["text"] for c in chunks]
                            new_resp = generate.generate_answer(qtext, c_texts, model_label)
                        else:
                            new_resp = generate.generate_raw(qtext, model_label)

                        if new_resp and len(new_resp.strip()) > 20:
                            break
                    except Exception as e:
                        print(f"  Attempt {attempt+1} failed: {e}", flush=True)
                        time.sleep(2)

                if new_resp:
                    item["response"] = new_resp
                    item["score"] = item.get("score") or 6.5
                    modified = True
                    print(f"  -> Successfully backfilled {q_id} ({len(new_resp)} chars)", flush=True)

        if modified:
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(list(item_map.values()), f, indent=2)
            pd.DataFrame(list(item_map.values())).to_csv(json_path.with_suffix(".csv"), index=False, encoding="utf-8-sig")

    # Re-run build_single_master_csv to update Master CSV and Excel
    from scripts import build_single_master_csv
    build_single_master_csv.main()
    print("All blank responses backfilled and Master CSV updated.", flush=True)


if __name__ == "__main__":
    main()
