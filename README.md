# 🏛️ SEBI Compliance AI & RAG Evaluation Suite
> **PGPBA Term 4 Generative AI Endterm Project — Domain #3: SEBI & Capital Markets Regulations**

An enterprise-grade, retrieval-augmented compliance assistant designed to answer complex Indian capital markets queries grounded in primary statutory regulations. The system addresses critical hallucination traps in general LLMs by combining hybrid dense-sparse retrieval (ChromaDB + BM25) with legal document chunking and source citation.

---

## 📌 Table of Contents
1. [Project Overview](#-project-overview)
2. [Key Features & Enhancements](#-key-features--enhancements)
3. [System Architecture](#-system-architecture)
4. [Directory & File Map](#-directory--file-map)
5. [Statutory Knowledge Base Coverage](#-statutory-knowledge-base-coverage)
6. [50-Question SEBI Benchmark Design](#-50-question-sebi-benchmark-design)
7. [Dependencies & Technical Stack](#-dependencies--technical-stack)
8. [Installation & Setup](#-installation--setup)
9. [Running the Application (1-Click Auto Launch)](#-running-the-application-1-click-auto-launch)
10. [Running Benchmark & Evaluation Scripts](#-running-benchmark--evaluation-scripts)
11. [Submission Deliverables Summary](#-submission-deliverables-summary)

---

## 📖 Project Overview

General-purpose Large Language Models frequently fail on Indian regulatory compliance due to outdated training cutoffs, generic global bias, and hallucinated statutory limits (e.g., misstating promoter lock-in periods or open offer threshold limits under SEBI rules).

This repository addresses those limitations by building a domain-specific compliance assistant backed by a 50-question evaluation benchmark calibrated across 5 difficulty tiers. The system grounds its answers in primary SEBI Acts, Regulations, and Master Circulars, providing inline legal citations and relevance scores.

---

## ✨ Key Features & Enhancements

* **Primary SEBI Legal Knowledge Base:** 11 full statutory legal text files covering 7 major SEBI operational domains (PIT, SAST, ICDR, LODR, AIF, Mutual Funds, FPI).
* **Hybrid Retrieval Engine:** Combines dense semantic vector embeddings (`sentence-transformers/all-MiniLM-L6-v2`, `all-mpnet-base-v2`, `bge-small-en-v1.5`) with sparse BM25 keyword matching, controlled by a real-time hybrid weight slider ($\alpha$).
* **50-Question SEBI Calibration Benchmark:** A dataset spanning 5 difficulty tiers—from factual recall (Tier 1) to multi-step reasoning (Tier 4) and adversarial traps (Tier 5).
* **Dark Glassmorphism Web Interface (`ui/gradio_app.py`):**
  * **Tab 1:** Interactive Compliance Query Assistant with source chunk viewing and latency breakdown.
  * **Tab 2:** Live Head-to-Head Explorer (Base Un-augmented LLM vs. Hybrid RAG System).
  * **Tab 3:** Knowledge Base Document Lab for uploading and managing custom regulatory files.
* **Self-Healing LLM Engine (`backend/generate.py`):** Multi-model wrapper supporting OpenAI (`gpt-4o-mini`, `gpt-5-nano`) and Together AI (`mistralai/Mistral-7B-Instruct-v0.1`, `gemma-3n`) with automatic fallback to prevent API errors.
* **Architectural Isolation (`predictive/`):** Dedicated directory at the project root for non-Generative AI machine learning models.

---

## 🏗️ System Architecture

```
                               ┌───────────────────────────┐
                               │     User Query / Web UI   │
                               └─────────────┬─────────────┘
                                             │
                                             ▼
                               ┌───────────────────────────┐
                               │   FastAPI Server (main)   │
                               └─────────────┬─────────────┘
                                             │
                       ┌─────────────────────┴─────────────────────┐
                       ▼                                           ▼
         ┌───────────────────────────┐               ┌───────────────────────────┐
         │  Dense Vector Search      │               │   Sparse BM25 Keyword     │
         │  (ChromaDB / MiniLM-L6)   │               │   Search (Rank-BM25)      │
         └─────────────┬─────────────┘               └─────────────┬─────────────┘
                       │                                           │
                       └─────────────────────┬─────────────────────┘
                                             │ Hybrid Score Blending (alpha)
                                             ▼
                               ┌───────────────────────────┐
                               │ Top-K Statutory Chunks    │
                               └─────────────┬─────────────┘
                                             │
                                             ▼
                               ┌───────────────────────────┐
                               │ LLM Generation Engine     │
                               │ (OpenAI / Together AI)    │
                               └─────────────┬─────────────┘
                                             │
                                             ▼
                               ┌───────────────────────────┐
                               │ Grounded Compliance Answer│
                               │ + Source Citations [1][2] │
                               └───────────────────────────┘
```

---

## 📁 Directory & File Map

```
pgai-et/
├── backend/                                   # Core RAG backend logic
│   ├── config.py                              # Configuration tokens & model mappings
│   ├── chunking.py                            # Recursive text splitter implementation
│   ├── keyword_search.py                      # BM25 Okapi scorer for sparse retrieval
│   ├── vectorstore.py                         # ChromaDB collections & hybrid search fusion
│   ├── ingest.py                              # PDF, DOCX, TXT text extraction engine
│   ├── generate.py                            # OpenAI & Together AI completion wrappers
│   ├── schemas.py                             # Pydantic request & response models
│   └── main.py                                # FastAPI application entrypoint
├── ui/
│   └── gradio_app.py                          # Gradio web interface (3 tabs)
├── data/
│   ├── sebi_documents/                        # Primary SEBI statutory legal text files
│   ├── uploads/                               # Ingested document storage
│   ├── chroma/                                # Persistent ChromaDB vector database index
│   └── benchmark/                             # 50-Question benchmark & Excel deliverables
│       ├── sebi_benchmark_50.json
│       ├── sebi_benchmark_50.csv
│       ├── sebi_benchmark_50.jsonl
│       └── SEBI_Compliance_AI_Benchmark_Deliverable_A_Full.xlsx
├── reports/                                   # Course deliverables
│   ├── SEBI_Compliance_AI_Report.md           # 10-Page Group Report (Deliverable B)
│   └── SEBI_Compliance_AI_Presentation.md     # Pitch Deck & Demo Walkthrough (Deliverable C)
├── scripts/                                   # Data curation & evaluation tools
│   ├── download_sebi_documents_comprehensive.py # Statutory text generator & multi-model indexer
│   ├── build_sebi_benchmark.py                # 50-Question benchmark dataset builder
│   ├── build_full_scored_excel_deliverable.py # Deliverable A Excel workbook generator
│   └── evaluate_sebi_benchmark.py             # Batch benchmark evaluator runner
├── predictive/                                # Isolated directory for predictive ML models
│   └── .gitkeep
├── run.bat                                    # 1-Click Windows automatic launcher script
├── run.sh                                     # 1-Click Linux/macOS automatic launcher script
├── .env                                       # Environment variables & API keys
├── requirements.txt                           # Python project dependencies
└── README.md                                  # Complete project documentation
```

---

## 📜 Statutory Knowledge Base Coverage

The knowledge base in `data/sebi_documents/` contains legal texts covering 7 core SEBI operational domains:

1. **SEBI (PIT) Regulations, 2015:** Insider Trading, UPSI definitions, trading window closure, designated persons, Structured Digital Database (SDD) requirements.
2. **SEBI (SAST) Regulations, 2011:** Takeover Code, 25% open offer trigger, 5% creeping acquisition limit, Regulation 10 exemptions, escrow account calculations.
3. **SEBI (ICDR) Regulations, 2018:** Main Board IPO Regulation 6(1)/6(2), SME IPO Chapter IX, 20% minimum promoter contribution, 18-month lock-in, QIP rules.
4. **SEBI (LODR) Regulations, 2015:** Regulation 17 board composition, Regulation 23 related party transactions, Regulation 30 material event disclosures (Schedule III).
5. **SEBI (AIF) Regulations, 2012:** Category I, II, and III fund classifications, 25% investible funds cap, Category III 2x NAV leverage cap, Angel Funds Regulation 19.
6. **SEBI (Mutual Funds) Regulations, 1996 & Master Circular 2024:** Regulation 52 Total Expense Ratio (TER) limits, ESG thematic fund framework, redemption suspension rules.
7. **SEBI (FPI) Regulations, 2019:** Single FPI <10% equity holding cap, automatic FDI reclassification provisions under FEMA.

---

## 🎯 50-Question SEBI Benchmark Design

The evaluation benchmark in `data/benchmark/sebi_benchmark_50.json` is organized across 5 difficulty tiers (10 questions each):

| Tier | Category | Description | Example Target |
| :---: | :--- | :--- | :--- |
| **Tier 1** | Factual Recall | Direct numerical thresholds & timelines | Disclosure thresholds under SEBI PIT Reg 7(2) |
| **Tier 2** | Conceptual Distinctions | Distinguishing related legal mechanisms | Creeping Acquisition vs. Voluntary Open Offer |
| **Tier 3** | Scenario Applications | Real-world compliance situations | Board financial result disclosure timelines (30 min) |
| **Tier 4** | Multi-Step Reasoning | Multi-clause legal analysis | IPO eligibility fallbacks via QIB book-building |
| **Tier 5** | Adversarial Traps | Common LLM hallucination traps | Rejecting invalid 72-hour insider disclosure rules |

---

## 📦 Dependencies & Technical Stack

All required Python packages are pinned in [`requirements.txt`](file:///C:/Users/pavan/workspace/iimb/pgai-et/requirements.txt):

| Category | Package | Purpose |
| :--- | :--- | :--- |
| **Web Server** | `fastapi>=0.110`, `uvicorn[standard]>=0.27` | High-performance REST API backend |
| **User Interface** | `gradio>=4.36` | Interactive 3-tab web dashboard & queue engine |
| **Vector Database** | `chromadb>=0.5.0` | Local persistent embedding database |
| **Embeddings** | `sentence-transformers>=2.7` | CPU PyTorch dense vector encoder models |
| **Text Extractors** | `pypdf>=4.2`, `python-docx>=1.1` | Multiformat file parser engine for PDFs and Word docs |
| **LLM Clients** | `openai>=1.0` | OpenAI & Together AI API client wrappers |
| **Data & Metrics** | `pandas`, `scikit-learn`, `joblib` | Data analysis, tabular data manipulation, predictive models |
| **Excel Export** | `openpyxl` | Multi-tab formatted Excel deliverable generator |
| **Environment** | `python-dotenv>=1.0`, `pydantic>=2.6` | `.env` variable configuration & schema validation |

---

## 💻 Installation & Setup

### Prerequisites
* Python 3.10+ (Python 3.11/3.13 recommended)
* Git

### Step-by-Step Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/pkulkarni245/llm-benchmark-proj.git
   cd llm-benchmark-proj
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows (PowerShell)
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

   # Linux / macOS
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install all dependencies from requirements.txt:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Create or edit the `.env` file in the root directory:
   ```env
   OPENAI_API_KEY="your-openai-api-key"
   TOGETHER_API_KEY="your-together-api-key"
   ```

---

## 🚀 Running the Application (1-Click Auto Launch)

For zero-configuration startup, anyone cloning the repository can launch the application with a single click:

### Option A: 1-Click Automated Script (Recommended)
* **Windows:** Double-click `run.bat` or run `.\run.bat` in CMD/PowerShell.
* **Linux / macOS:** Run `chmod +x run.sh && ./run.sh`.

*The 1-click script automatically detects Python, creates `.venv` if missing, installs dependencies from `requirements.txt` quietly, and launches the web server.*

### Option B: Manual CLI Launch
```bash
python -m backend.main
```

Once started, navigate to:
👉 **`http://localhost:7860/`** (or `http://127.0.0.1:7860/`)

### Using the Interface
* **Tab 1 (Compliance Assistant):** Type any SEBI regulatory question, select your preferred embedding and LLM models, adjust the hybrid search slider ($\alpha$), and click **Search & Generate Compliance Answer**.
* **Tab 2 (Head-to-Head Explorer):** Select a question from the 50-question benchmark dropdown to compare the **Base LLM** response against the **RAG System** response side-by-side.
* **Tab 3 (Knowledge Base Lab):** Upload custom regulatory documents or clear/re-ingest active vector collections.

---

## 📊 Running Benchmark & Evaluation Scripts

### 1. Ingest Full Statutory Documents into ChromaDB
To re-generate the primary legal texts and populate all 3 embedding collections (`MiniLM-L6`, `MPNet-base`, `BGE-small`):
```bash
python -m scripts.download_sebi_documents_comprehensive
```

### 2. Build / Refresh the 50-Question Benchmark Dataset
To re-generate the JSON, CSV, and JSONL benchmark files:
```bash
python -m scripts.build_sebi_benchmark
```

### 3. Generate the Deliverable A Excel Workbook
To generate the multi-tab Excel workbook with individual scorer sheets:
```bash
python -m scripts.build_full_scored_excel_deliverable
```
The output file will be saved at:
`data/benchmark/SEBI_Compliance_AI_Benchmark_Deliverable_A_Full.xlsx`

### 4. Run Batch Benchmark Evaluation across Models
To run all 50 questions through the evaluation pipeline:
```bash
python -m scripts.evaluate_sebi_benchmark
```

---

## 📑 Submission Deliverables Summary

| Deliverable | Description | File Location |
| :--- | :--- | :--- |
| **Deliverable A** | Multi-Tab Scored Excel Workbook | [`data/benchmark/SEBI_Compliance_AI_Benchmark_Deliverable_A_Full.xlsx`](file:///C:/Users/pavan/workspace/iimb/pgai-et/data/benchmark/SEBI_Compliance_AI_Benchmark_Deliverable_A_Full.xlsx) |
| **Deliverable B** | 10-Page Academic Group Report | [`reports/SEBI_Compliance_AI_Report.md`](file:///C:/Users/pavan/workspace/iimb/pgai-et/reports/SEBI_Compliance_AI_Report.md) |
| **Deliverable C** | Presentation Deck & Script | [`reports/SEBI_Compliance_AI_Presentation.md`](file:///C:/Users/pavan/workspace/iimb/pgai-et/reports/SEBI_Compliance_AI_Presentation.md) |
| **Benchmark Data** | 50-Question Dataset | [`data/benchmark/sebi_benchmark_50.json`](file:///C:/Users/pavan/workspace/iimb/pgai-et/data/benchmark/sebi_benchmark_50.json) |
| **Source Documents** | Primary Statutory Text Files | [`data/sebi_documents/`](file:///C:/Users/pavan/workspace/iimb/pgai-et/data/sebi_documents) |

---

## 🤝 Project Credits & Acknowledgments
* **Course:** PGPBA Term 4 — Advanced Generative AI & RAG Engineering
* **Domain Assignment:** Domain #3 — SEBI & Capital Markets Regulations (Indian Context)
* **Architecture:** Hybrid Dense-Sparse Retrieval RAG with ChromaDB & BM25
