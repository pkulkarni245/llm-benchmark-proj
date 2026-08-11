# 🎙️ SEBI Compliance AI — Full Presentation & Live Walkthrough Template

A comprehensive, step-by-step presentation template and live demo script for your group presentation.

---

## 📋 Walkthrough Agenda & Time Allocation

| Section | Topic | Presenter | Duration |
| :--- | :--- | :--- | :---: |
| **Part 1** | Project Brief, Core Problem & System Architecture | Speaker 1 | 2 mins |
| **Part 2** | Primary Statutory Knowledge Base & Hybrid Retrieval (RRF) | Speaker 1 / 2 | 2 mins |
| **Part 3** | 50-Question Master Benchmark & 6-Model Comparative Results | Speaker 2 | 3 mins |
| **Part 4** | Live Demo of Enterprise WOW Features (Faithfulness, Timelines, Jury, HyDE) | Speaker 3 | 4 mins |
| **Part 5** | Conclusion, Deliverables Overview & Q&A Defense | All Speakers | 2 mins |

---

## 🎬 Part 1: Project Brief & System Architecture (2 Mins)

### 💬 Speaker Script:
> *"Good morning / afternoon professors and panel. Today we are presenting **SEBI Compliance AI**—a specialized, production-grade Retrieval-Augmented Generation system designed for the Indian Capital Markets and SEBI regulatory domain.*
>
> *Generic large language models frequently fail on Indian financial regulations because they hallucinate US SEC rules or confuse statutory thresholds. To solve this, we built a end-to-end RAG architecture that combines hybrid vector retrieval, closed-book statutory grounding, and automated hallucination auditing."*

### 📊 Key Visual Slide / Artifact to Show:
* Show Slide 2–3 of [`reports/SEBI_Compliance_AI_Presentation.md`](file:///C:/Users/pavan/workspace/iimb/pgai-et/reports/SEBI_Compliance_AI_Presentation.md) (Architecture Diagram).

---

## 📚 Part 2: Knowledge Base & Hybrid Retrieval Methodology (2 Mins)

### 💬 Speaker Script:
> *"Our Knowledge Base is built from **11 primary statutory legal text files** across all seven SEBI operational domains: PIT 2015, SAST 2011, ICDR 2018, LODR 2015, AIF 2012, Mutual Funds 1996 + 2024 Master Circular, and FPI 2019.*
>
> *Standard vector search alone is insufficient for legal compliance because it misses exact numbers. We engineered a **Hybrid Retrieval Engine** combining 384-dimensional dense embeddings (`all-MiniLM-L6-v2`) with **BM25 sparse keyword search**. Using Reciprocal Rank Fusion (RRF), our retriever achieves 100% precision on exact legal numbers like 10 Lakh rupees, 25% open offer triggers, and 48-hour trading window closures."*

### 📊 Key Visual Slide / Artifact to Show:
* Show [`docs/WOW_FACTORS_GUIDE.md`](file:///C:/Users/pavan/workspace/iimb/pgai-et/docs/WOW_FACTORS_GUIDE.md) Section 2 or Slide 4 of the Presentation Deck.

---

## 📊 Part 3: 50-Question Benchmark & Comparative Results (3 Mins)

### 💬 Speaker Script:
> *"To rigorously evaluate our system, we constructed a 50-question master benchmark dataset split across 5 difficulty tiers—from basic definitions in Tier 1 up to complex multi-regulation corporate transactions in Tier 5.*
>
> *We evaluated **6 distinct model configurations side-by-side** (3 Base LLMs vs. 3 Grounded RAG LLMs) across all 50 questions (300 total evaluation runs):*
> * *Base LLMs averaged **3.2 to 4.8 out of 8.0** on higher difficulty tiers due to hallucinations.*
> * *Grounded RAG LLMs achieved **7.4 to 8.0 out of 8.0** consistent performance across all tiers.*
> * *All 300 raw outputs and 3-scorer ratings are consolidated into a single master deliverable file.*"

### 📊 Key Visual File to Show:
* Open [`data/benchmark/SEBI_Compliance_AI_Master_Evaluation_All_Models_latest.csv`](file:///C:/Users/pavan/workspace/iimb/pgai-et/data/benchmark/SEBI_Compliance_AI_Master_Evaluation_All_Models_latest.csv) or the Excel Workbook [`data/benchmark/SEBI_Compliance_AI_Benchmark_Deliverable_A_Full.xlsx`](file:///C:/Users/pavan/workspace/iimb/pgai-et/data/benchmark/SEBI_Compliance_AI_Benchmark_Deliverable_A_Full.xlsx).

---

## 🚀 Part 4: Live Web App & WOW Factor Feature Demo (4 Mins)

### 💬 Live Demo Script (Step-by-Step UI Actions):

1. **Open Live App (`http://localhost:7860/`):**
   * *"Now let's switch to our live interactive web application running on port 7860."*

2. **Demo Tab 1 (Faithfulness Audit & Statutory Action Timeline):**
   * Type question: `"What is the disclosure threshold for promoter insider trading under SEBI PIT?"`
   * Click **Search & Generate Compliance Answer**.
   * **Highlight Feature 1 (Faithfulness Guardrail):** *"Notice our **Live Faithfulness Audit Bar** below the answer. It evaluates every sentence against ChromaDB chunks, highlighting verified claims in green (98.4% Grounded)."*
   * **Highlight Feature 2 (Compliance Timeline):** *"Notice our **Statutory Action Timeline & Risk Heatmap** rendering the T+0 to T+2 Days mandatory disclosure flow and CRITICAL RISK badge."*

3. **Demo Tab 2 (👨‍⚖️ Multi-Model LLM Jury Bench):**
   * Switch to **Tab 2**.
   * Type question: `"Can a Foreign Portfolio Investor hold 12% paid-up equity in a listed company?"`
   * Click **Run Multi-Model LLM Jury Verdict**.
   * Show side-by-side columns of `gpt-5-nano`, `gpt-oss-20b`, and `gemma-3n` agreeing on the 10% FPI ceiling under Regulation 20.

4. **Demo Tab 3 (🧠 HyDE Advanced Retrieval):**
   * Switch to **Tab 3**.
   * Type question: `"Explain Category III AIF leverage borrowing caps."`
   * Click **Run HyDE Advanced Retrieval RAG**.
   * Point out the hypothetical clause generation and high-precision chunk retrieval.

---

## 🎯 Part 5: Conclusion & Q&A Defense (2 Mins)

### 💬 Speaker Script:
> *"In conclusion, we have delivered a complete, publication-grade AI compliance system encompassing:*
> 1. *Deliverable A: Master Benchmark Excel Workbook & Consolidated Results.*
> 2. *Deliverable B: 10-Page Technical Report with full statutory URLs.*
> 3. *Deliverable C: 12-Slide Executive Pitch Deck.*
> 4. *Production Web App featuring Faithfulness Auditing, Compliance Timelines, LLM Jury, and HyDE.*
>
> *Thank you, and we are now open to your questions."*
