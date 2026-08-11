"""CLI: run a set of inputs through an OpenAI-compatible LLM endpoint.

Input is a JSONL file where each line is an object with either:
  {"prompt": "..."}
  {"question": "...", "chunks": ["...", "..."]}

Output is a JSONL file with the original fields plus a "response" field.

Usage (from repo root):
    python -m scripts.generate_llm --input in.jsonl --output out.jsonl \
        --model "gpt-5-nano (OpenAI)"
"""
import argparse
import json

from dotenv import load_dotenv

from backend.config import ANSWER_MODELS, DEFAULT_ANSWER_MODEL
from backend.generate import generate_answer, generate_raw, is_configured

load_dotenv()


def _read_inputs(path: str) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def _run_one(record: dict, answer_model_label: str) -> str:
    if "chunks" in record:
        return generate_answer(record["question"], record["chunks"], answer_model_label)
    return generate_raw(record["prompt"], answer_model_label)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Path to input JSONL file")
    parser.add_argument("--output", required=True, help="Path to write output JSONL file")
    parser.add_argument(
        "--model",
        default=DEFAULT_ANSWER_MODEL,
        choices=list(ANSWER_MODELS),
        help="Answer model label from backend.config.ANSWER_MODELS",
    )
    args = parser.parse_args()

    if not is_configured(args.model):
        spec = ANSWER_MODELS[args.model]
        raise SystemExit(f"Missing API key: set {spec['api_key_env']} in your environment")

    records = _read_inputs(args.input)
    with open(args.output, "w", encoding="utf-8") as out:
        for record in records:
            response = _run_one(record, args.model)
            out.write(json.dumps({**record, "response": response}) + "\n")

    print(f"Wrote {len(records)} responses to {args.output}")


if __name__ == "__main__":
    main()
