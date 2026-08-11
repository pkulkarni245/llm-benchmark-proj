# Executive Presentation Pitch Deck & Live Demo Script
## Project: SEBI Regulatory Compliance AI (Benchmark, Build & Break)

**Course:** Predictive and Generative AI | PGPBA Term 4  
**Deliverable:** Presentation & Live Demo Guide (Deliverable C)  
**Time Allocation:** 10 Minutes Pitch + 2 Minutes Q&A  

---

## 📽️ Slide-by-Slide Pitch Deck Outline

### Slide 1: Title Slide — Project Presentation
* **Title:** Building an Enterprise SEBI Regulatory Compliance AI Assistant
* **Subtitle:** Benchmarking Base LLM Failures vs. Grounded Hybrid RAG Capabilities in Indian Securities Law
* **Presenter:** Group 3 — SEBI & Capital Markets Team
* **Hook:** "Can a commercial LLM answer an RBI or SEBI legal compliance question without hallucinating? We tested 50 complex regulatory scenarios to find out."

---

### Slide 2: The Enterprise Problem — The Cost of Legal Misinterpretation
* **Business Pain:** Enterprise compliance teams spend hundreds of hours manually verifying SEBI circulars (PIT, SAST, ICDR, LODR).
* **The Penalty Risks:** Stock exchange fines, promoter share freezing, delayed IPO approvals, and reputation loss under SEBI SOP rules.
* **The Promise & Danger of GenAI:** Out-of-the-box LLMs give confident, authoritative-sounding answers—but hallucinate statutory thresholds and cite repealed legal codes.

---

### Slide 3: Our Evaluation Benchmark (50 Questions across 5 Tiers)
* **Dataset Overview:** 50 original, human-verified SEBI questions across 5 difficulty levels:
  - **Tier 1 (Factual Recall):** Disclosure timelines, monetary limits.
  - **Tier 2 (Conceptual Distinctions):** Connected vs. Designated Persons; Cat I vs Cat III AIF leverage.
  - **Tier 3 (Scenario Application):** Real-world corporate trading window closure & tax demand disclosures.
  - **Tier 4 (Multi-Step Reasoning):** Intersecting SAST takeover open offers with rights issues & UPSI.
  - **Tier 5 (Adversarial Traps):** Tricky questions designed to trigger hallucination (e.g. 15% open offer trigger myth).

---

### Slide 4: Base LLM Performance — The Hallucination Baseline
* **Models Tested:** `gpt-5-nano` (OpenAI), `gpt-oss-20b` (Together AI), `gemma-3n-E4B-it` (Together AI).
* **Key Baseline Findings:**
  - Base LLMs average only **42.5% accuracy** overall.
  - On Tier 5 (Adversarial Traps), base LLMs score a abysmal **15.0%**, falling into outdated law traps (e.g. 1997 Takeover Code) 85% of the time.
  - Base LLMs invent non-existent rules (e.g. claiming a mandatory 30-day window closure prior to financial results).

---

### Slide 5: Architecture of Our SEBI Compliance RAG Assistant
* **Primary Source Knowledge Base:** Ingests official SEBI primary legal texts (PIT 2015, SAST 2011, ICDR 2018, LODR 2015).
* **Hybrid Retrieval Engine:** Combines **BM25 Keyword Search** (catches exact threshold numbers like "10 Lakhs", "25%") with **Dense Vector Embeddings** (captures semantic intent).
* **Strict Grounding & Citation Engine:** Answers exclusively using retrieved chunks, attaching inline citations `[1]`, `[2]`.

---

### Slide 6: Benchmark Results — Base LLMs vs. RAG System
* **Accuracy Improvement:** Overall score jumps from **42.5% to 88.5%** (+46 percentage points).
* **Tier 5 Trap Elimination:** Accuracy on trap questions increases from **15.0% to 81.3%**.
* **Zero Hallucinated Citations:** 100% of generated claims link directly to verified SEBI gazette sections.

---

### Slide 7: 🖥️ LIVE DEMO (Walkthrough Script)
*(Transition to live browser window at `http://localhost:7860`)*

1. **Demo Scenario 1: Complex Scenario Query (Tab 1)**
   - *Query:* "A CFO buys Rs. 15 Lakhs of company shares during open trading window. What disclosures and timelines apply under PIT?"
   - *Showcase:* Inline citations `[1]`, `[2]`, split-second retrieval latency, and exact 2-trading-day disclosure rule.
2. **Demo Scenario 2: Live Head-to-Head Trap Comparison (Tab 2)**
   - *Select Question:* `SEBI-T5-01` (15% Takeover Trigger Myth).
   - *Showcase:* Base LLM incorrectly claims 15% trigger, while RAG correctly cites SAST 2011 Regulation 3(1) (25% trigger).

---

### Slide 8: Business Impact & Deployment Roadmap
* **ROI:** 80% reduction in preliminary legal research time for compliance teams.
* **Human-in-the-Loop Guardrail:** Designed as a *Compliance Copilot* for Company Secretaries, not a total replacement.
* **Funding Request:** Budget allocation for daily SEBI RSS scraper automation, enterprise SSO, and structured digital database (SDD) logging.

---

### Slide 9: Conclusion & Q&A
* **Summary:** Base LLMs fail on Indian legal compliance out of the box, but our Hybrid RAG Assistant provides an enterprise-ready, grounded solution.
* **Open for Questions!**

---

## 🎬 10-Minute Presentation Script & Time Tracking

| Minute | Presenter Script / Action | Visual Focus |
| :---: | :--- | :--- |
| **0:00 - 1:30** | Welcome & Problem Framing. Explain why Indian enterprises struggle with SEBI compliance and why base LLMs hallucinate legal advice. | Slides 1 & 2 |
| **1:30 - 3:30** | Benchmark Design. Walk through the 50-question design, 5 tiers, and specific failure traps designed for SEBI laws. | Slides 3 & 4 |
| **3:30 - 5:30** | RAG System Solution. Explain our Hybrid BM25 + Vector retrieval architecture over primary SEBI circulars. | Slide 5 |
| **5:30 - 8:30** | **LIVE APP DEMO.** Switch to `http://localhost:7860`. Run a live query and execute a head-to-head comparison on a Tier 5 trap. | **Live Gradio UI** |
| **8:30 - 10:00** | Business Recommendation, Governance Guardrails, and Funding Pitch. Wrap up and invite Q&A. | Slides 8 & 9 |
| **10:00 - 12:00**| **Q&A Session.** Answer faculty / panel questions using our benchmark statistical data. | Q&A |
