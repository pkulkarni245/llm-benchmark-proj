"""Comprehensive Automated Test Suite for All 4 WOW Factor Features:
1. Faithfulness & Hallucination Audit Engine
2. Statutory Compliance Action Timeline & Risk Heatmap
3. Multi-Model LLM Jury Consensus Bench
4. HyDE Advanced Query Rewriter
"""
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

from backend import consensus, faithfulness, hyde, timeline


def test_all_features():
    print("\n=======================================================")
    print(" RUNNING EMPIRICAL TEST SUITE FOR ALL WOW FEATURES")
    print("=======================================================\n")

    sample_question = "What is the mandatory disclosure threshold for promoter insider trading under SEBI PIT Regulations?"
    sample_context = [
        "SEBI (PIT) Regulations, 2015 - Regulation 7(2)(a): Every promoter, member of promoter group, designated person and director shall disclose to the company the number of securities acquired or disposed of within two trading days if the traded value over any calendar quarter exceeds ten lakh rupees (Rs 10 Lakhs)."
    ]
    sample_response = "Under Regulation 7(2)(a) of SEBI PIT Regulations 2015, every promoter must disclose acquisitions or disposals exceeding Rs 10 Lakhs within two trading days of the transaction."

    # 1. Test Faithfulness Engine
    print("--- 1. Testing Faithfulness & Hallucination Audit Engine ---")
    audit_res = faithfulness.audit_faithfulness(sample_response, sample_context)
    print(f"  Score Percentage: {audit_res['score_percentage']}%")
    print(f"  Status Label:     {audit_res['status_label']}")
    print(f"  Verified Count:   {audit_res['verified_count']}/{audit_res['total_sentences']}")
    assert audit_res["score_percentage"] > 80.0, "Faithfulness score test failed!"
    print("  PASSED: Faithfulness Engine Test PASSED cleanly.\n")

    # 2. Test Timeline & Risk Heatmap Engine
    print("--- 2. Testing Statutory Action Timeline & Risk Heatmap ---")
    timeline_res = timeline.extract_timeline_and_risk(sample_response, sample_question)
    print(f"  Risk Level:       {timeline_res['risk_level']}")
    print(f"  Detected Events:  {[e['step'] for e in timeline_res['events']]}")
    assert timeline_res["risk_level"] == "CRITICAL COMPLIANCE REGIME", "Risk detection failed!"
    assert len(timeline_res["events"]) >= 2, "Timeline extraction failed!"
    print("  PASSED: Statutory Timeline & Risk Heatmap Test PASSED cleanly.\n")

    # 3. Test LLM Jury Consensus Engine
    print("--- 3. Testing Multi-Model LLM Jury Consensus Bench ---")
    jury_res = consensus.run_llm_jury_consensus(sample_question, sample_context)
    print(f"  Consensus Status: {jury_res['consensus_status']}")
    print(f"  Agreement Score:  {jury_res['consensus_score']}%")
    print(f"  Opinions Count:   {len(jury_res['opinions'])} models")
    assert len(jury_res["opinions"]) == 3, "Jury missing model opinions!"
    print("  PASSED: LLM Jury Consensus Bench Test PASSED cleanly.\n")

    # 4. Test HyDE Query Rewriter
    print("--- 4. Testing HyDE Advanced Retrieval Pipeline ---")
    hyde_res = hyde.run_hyde_rag_pipeline(sample_question, "gpt-5-nano (OpenAI)")
    print(f"  Hypothetical Doc: {hyde_res['hypothetical_document'][:100]}...")
    print(f"  Chunks Retrieved: {len(hyde_res['retrieved_chunks'])}")
    print(f"  Final Answer Len: {len(hyde_res['final_answer'])} chars")
    assert len(hyde_res["final_answer"]) > 20, "HyDE answer generation failed!"
    print("  PASSED: HyDE Advanced Query Rewriter Test PASSED cleanly.\n")

    print("=======================================================")
    print(" ALL 4 WOW FEATURE EMPIRICAL TESTS PASSED 100%!")
    print("=======================================================\n")


if __name__ == "__main__":
    test_all_features()
