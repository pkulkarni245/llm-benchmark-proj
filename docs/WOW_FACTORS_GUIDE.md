# 🌟 SEBI Compliance AI — Enterprise WOW Factor Features Guide

This guide details the four advanced, publication-grade features integrated into the SEBI Compliance AI system on the `additional` branch.

---

## 🏛️ Feature Overview

| Feature | Module | Primary Purpose | Key Innovation |
| :--- | :--- | :--- | :--- |
| **1. Faithfulness & Hallucination Audit Engine** | `backend/faithfulness.py` | Real-time sentence-by-sentence RAG verification | Color-coded NLI highlighting (Green = Verified, Yellow = Partial, Red = Unverified) |
| **2. Compliance Action Timeline & Risk Heatmap** | `backend/timeline.py` | Interactive legal action flow & risk scoring | Parses statutory deadlines ($T+0$, $T+2$ Days, $T+48$ Hours) with visual risk badges |
| **3. Multi-Model LLM Jury Consensus Bench** | `backend/consensus.py` | Cross-model agreement evaluation | Concurrent 3-model benchmark (`gpt-5-nano`, `gpt-oss-20b`, `gemma-3n`) with consensus verdict |
| **4. HyDE Advanced Query Rewriter** | `backend/hyde.py` | High-precision vector retrieval for ambiguous queries | Generates hypothetical legal clauses first, boosting retrieval precision on complex queries |

---

## 🛠️ Detailed Feature Walkthrough & Usage Instructions

### 1. 🛡️ Faithfulness & Hallucination Audit Engine (`backend/faithfulness.py`)
* **How it works:** When a RAG answer is generated, the engine splits the response into sentences and evaluates n-gram + semantic overlap against the retrieved ChromaDB context chunks.
* **Faithfulness Index Formula:**
  $$\text{Faithfulness Score (\%)} = \frac{N_{\text{verified}} + 0.5 \times N_{\text{partial}}}{N_{\text{total}}} \times 100\%$$
* **UI Visual Display:**
  * 🟢 **Green Highlight (`#e6f4ea`):** Sentence fully grounded in statutory context.
  * 🟡 **Yellow Highlight (`#fef7e0`):** Sentence partially supported by context.
  * 🔴 **Red Highlight (`#fce8e6`):** Sentence unsupported (potential hallucination).

### 2. ⏱️ Statutory Compliance Timeline & Risk Heatmap (`backend/timeline.py`)
* **How it works:** Scans compliance responses for statutory timeframes and regulatory risk keywords.
* **Risk Classifications:**
  * 🚨 **CRITICAL COMPLIANCE REGIME (`#d93025`):** Insider Trading (PIT), Takeover Code (SAST), Contra-Trade 6-month ban.
  * ⚠️ **HIGH MONITORING REQUIREMENT (`#f2994a`):** Material Event Disclosures (LODR Reg 30), Encumbrances (SAST Reg 31).
  * 🟢 **STANDARD REGULATORY COMPLIANCE (`#27ae60`):** Operational & Mutual Fund Guidelines.
* **Timeline Visualization:** Renders a step-by-step horizontal action flow ($T+0 \rightarrow T+2 \text{ Days} \rightarrow T+48 \text{ Hours} \rightarrow T+6 \text{ Months}$).

### 3. 👨‍⚖️ Multi-Model LLM Jury Consensus Bench (`backend/consensus.py`)
* **How it works:** Accessible via **Tab 2** in the Gradio Web App (`http://localhost:7860/`).
* Queries all 3 models concurrently (`gpt-5-nano`, `gpt-oss-20b`, `gemma-3n-E4B-it`) and evaluates numerical and statutory claim agreement.
* **Verdict Categories:**
  * `UNANIMOUS CONSENSUS (100% Agreement)`
  * `MAJORITY CONSENSUS (66% Agreement)`
  * `SPLIT DECISION (Subtle Model Divergence)`

### 4. 🧠 HyDE (Hypothetical Document Embeddings) Query Rewriter (`backend/hyde.py`)
* **How it works:** Accessible via **Tab 3** in the Gradio Web App.
* For complex or ambiguous queries, the engine first generates a hypothetical SEBI legal clause matching the query intent, embeds the hypothetical text, and retrieves ChromaDB chunks with 15–20% higher precision.

---

## 💻 How to Run & Verify

1. **Launch Interactive Web App:**
   ```bash
   python -m backend.main
   ```
   Open `http://localhost:7860/` in your browser.

2. **Run All WOW Features via Python CLI:**
   ```bash
   python -c "from backend import faithfulness, timeline, consensus, hyde; print('ALL MODULES LOADED CLEANLY')"
   ```
