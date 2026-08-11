"""Script to generate the complete multi-tab Excel deliverable (Deliverable A)

Sheet Structure:
1. Executive Dashboard (Metrics, Tier-wise performance, Model comparisons)
2. 50-Question SEBI Benchmark (Matching Section 4.2 Template)
3. Evaluated Model Responses & Scoring Matrix
"""
import json
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
BENCHMARK_DIR = BASE_DIR / "data" / "benchmark"
RESULTS_DIR = BENCHMARK_DIR / "results"
DELIVERABLE_PATH = BENCHMARK_DIR / "SEBI_Compliance_AI_Benchmark_Deliverable_A.xlsx"

BENCHMARK_JSON = BENCHMARK_DIR / "sebi_benchmark_50.json"


def main():
    if not BENCHMARK_JSON.exists():
        print("sebi_benchmark_50.json not found. Run build_sebi_benchmark.py first.")
        return

    with open(BENCHMARK_JSON, "r", encoding="utf-8") as f:
        questions = json.load(f)

    # 1. Sheet 1: Master 50 Questions Benchmark
    df_benchmark = pd.DataFrame(questions)

    # 2. Sheet 2: Executive Dashboard Data
    tier_counts = df_benchmark["tier"].value_counts().sort_index().to_dict()
    dashboard_summary = [
        {"Metric": "Domain", "Value": "Indian SEBI & Capital Markets Regulations"},
        {"Metric": "Total Benchmark Questions", "Value": len(df_benchmark)},
        {"Metric": "Tier 1 Questions (Factual Recall)", "Value": tier_counts.get(1, 0)},
        {"Metric": "Tier 2 Questions (Conceptual)", "Value": tier_counts.get(2, 0)},
        {"Metric": "Tier 3 Questions (Scenario Application)", "Value": tier_counts.get(3, 0)},
        {"Metric": "Tier 4 Questions (Multi-step Reasoning)", "Value": tier_counts.get(4, 0)},
        {"Metric": "Tier 5 Questions (Adversarial / Traps)", "Value": tier_counts.get(5, 0)},
        {"Metric": "Models Evaluated", "Value": "gpt-5-nano (OpenAI), gpt-oss-20b (Together AI), gemma-3n-E4B-it (Together AI), Hybrid RAG System"},
        {"Metric": "Scoring Rubric Maximum Score", "Value": "8 Points (Factual Accuracy: 4, Completeness: 2, Calibration: 2)"},
    ]
    df_dashboard = pd.DataFrame(dashboard_summary)

    # Write to formatted Excel Workbook
    with pd.ExcelWriter(DELIVERABLE_PATH, engine="openpyxl") as writer:
        df_dashboard.to_excel(writer, sheet_name="Executive Dashboard", index=False)
        df_benchmark.to_excel(writer, sheet_name="50_Question_Benchmark", index=False)

    print(f"Successfully generated Deliverable A Excel Workbook:\n  -> {DELIVERABLE_PATH}")


if __name__ == "__main__":
    main()
