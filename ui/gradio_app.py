import json
import time
from pathlib import Path

import gradio as gr

from backend import generate, ingest, vectorstore
from backend.chunking import split_text
from backend.config import (
    ANSWER_MODELS,
    DEFAULT_ANSWER_MODEL,
    DEFAULT_EMBEDDING_MODEL,
    EMBEDDING_MODELS,
)

BASE_DIR = Path(__file__).resolve().parent.parent
BENCHMARK_FILE = BASE_DIR / "data" / "benchmark" / "sebi_benchmark_50.json"

MODEL_CHOICES = list(EMBEDDING_MODELS.keys())
ANSWER_MODEL_CHOICES = ["None (retrieval only)"] + list(ANSWER_MODELS.keys())


def _load_benchmark_questions():
    if BENCHMARK_FILE.exists():
        with open(BENCHMARK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


BENCHMARK_DATA = _load_benchmark_questions()
QUESTION_CHOICES = [f"[{q['question_id']}] (Tier {q['tier']}) - {q['question_text'][:70]}..." for q in BENCHMARK_DATA]


def do_ingest(file, embedding_model, chunk_size, chunk_overlap):
    if file is None:
        return "Please select or upload a document first.", refresh_documents(embedding_model)

    with open(file.name, "rb") as f:
        raw = f.read()
    filename = file.name.split("/")[-1]

    text = ingest.extract_text(filename, raw)
    if not text.strip():
        return f"No extractable text found in '{filename}'.", refresh_documents(embedding_model)

    chunks = split_text(text, chunk_size=int(chunk_size), chunk_overlap=int(chunk_overlap))
    if not chunks:
        return "Chunking produced 0 chunks - try increasing chunk size.", refresh_documents(embedding_model)

    document_id = vectorstore.new_document_id()
    vectorstore.add_chunks(embedding_model, document_id, filename, chunks)

    status = f"Successfully ingested '{filename}' into {len(chunks)} chunks (Embedding Model: {embedding_model})."
    return status, refresh_documents(embedding_model)


def refresh_documents(embedding_model):
    docs = vectorstore.list_documents(embedding_model)
    rows = [[d["filename"], d["document_id"], d["num_chunks"]] for d in docs]
    return rows


def do_reset(embedding_model):
    vectorstore.reset_collection(embedding_model)
    return f"Cleared all documents for '{embedding_model}'.", refresh_documents(embedding_model)


def do_query(question, embedding_model, top_k, hybrid_weight, answer_model):
    if not question.strip():
        return "<p style='color:#ef4444;'>Please enter a compliance question.</p>", "", ""

    t0 = time.perf_counter()
    chunks = vectorstore.query(embedding_model, question, int(top_k), hybrid_weight)
    retrieval_ms = (time.perf_counter() - t0) * 1000

    if not chunks:
        chunk_md = "<div style='padding:12px; background:#fef2f2; border-left:4px solid #ef4444; border-radius:4px; color:#991b1b;'><strong>No matching regulatory chunks found in vectorstore.</strong> Make sure documents are ingested in Tab 3.</div>"
        return chunk_md, "_No context available_", f"Retrieval Latency: {retrieval_ms:.1f} ms"

    chunk_md_lines = []
    for i, c in enumerate(chunks, 1):
        score_badge = f"<span style='background:#dbeafe; color:#1e40af; padding:2px 8px; border-radius:12px; font-weight:600; font-size:12px;'>Relevance: {c['score']:.3f}</span>"
        chunk_md_lines.append(
            f"### Chunk [{i}] — {c['filename']} (Index: {c['chunk_index']}) {score_badge}\n\n"
            f"> {c['text']}\n"
        )
    chunk_md = "\n---\n".join(chunk_md_lines)

    answer = ""
    timing = f"Retrieval Latency: {retrieval_ms:.1f} ms"
    if answer_model != "None (retrieval only)":
        if not generate.is_configured(answer_model):
            answer = f"*No API key configured for {answer_model} in .env file — running in retrieval-only mode.*"
        else:
            t1 = time.perf_counter()
            answer = generate.generate_answer(question, [c["text"] for c in chunks], answer_model)
            gen_ms = (time.perf_counter() - t1) * 1000
            timing += f" | Generation ({answer_model}): {gen_ms:.1f} ms"

    return chunk_md, answer, timing


def load_benchmark_detail(selected_choice):
    if not selected_choice or not BENCHMARK_DATA:
        return "", "", "", "", ""
    
    idx = QUESTION_CHOICES.index(selected_choice)
    q = BENCHMARK_DATA[idx]
    
    header = f"### [{q['question_id']}] Tier {q['tier']} Question Details\n**Tier Type:** Tier {q['tier']}\n\n**Question:** {q['question_text']}"
    expected = f"**Statutory Expected Answer:**\n{q['expected_answer']}\n\n**Primary Legal Citation:** `{q['source_citation']}`\n**Official Gazette Link:** [{q['source_url']}]({q['source_url']})"
    trap = f"**Known LLM Hallucination Trap:**\n{q['known_trap']}" if q['tier'] == 5 else "*No specific trap defined for this tier.*"

    return header, expected, trap, q['question_text']


def run_benchmark_head_to_head(question_text, answer_model_choice):
    if not question_text.strip():
        return "Enter question first.", "Enter question first."

    # 1. Base LLM Response
    t0 = time.perf_counter()
    try:
        base_resp = generate.generate_raw(question_text, answer_model_choice)
        base_time = (time.perf_counter() - t0) * 1000
        base_md = f"**Base {answer_model_choice} Response** *(Latency: {base_time:.0f} ms)*:\n\n{base_resp}"
    except Exception as e:
        base_md = f"Error executing Base LLM: {str(e)}"

    # 2. RAG System Response
    t1 = time.perf_counter()
    try:
        chunks = vectorstore.query(DEFAULT_EMBEDDING_MODEL, question_text, top_k=4, hybrid_weight=0.5)
        if chunks:
            rag_resp = generate.generate_answer(question_text, [c["text"] for c in chunks], answer_model_choice)
            rag_time = (time.perf_counter() - t1) * 1000
            rag_md = f"**RAG System ({answer_model_choice} + BM25/Vector)** *(Latency: {rag_time:.0f} ms)*:\n\n{rag_resp}\n\n---\n*Retrieved {len(chunks)} grounded regulatory chunks.*"
        else:
            rag_md = "No matching chunks found in RAG vectorstore."
    except Exception as e:
        rag_md = f"Error executing RAG System: {str(e)}"

    return base_md, rag_md


def build_ui(app):
    with gr.Blocks(title="SEBI Compliance AI Lab") as demo:
        gr.HTML(
            """
            <div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #f8fafc; padding: 24px; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);">
                <h1 style="color: #38bdf8; font-size: 28px; margin-bottom: 6px;">Indian Regulatory Compliance AI: SEBI & Capital Markets</h1>
                <p style="color: #94a3b8; font-size: 15px;">PGPBA Term 4 Project Lab — Benchmark, Build & Break RAG Compliance Assistant</p>
            </div>
            """
        )

        with gr.Tab("1. Compliance Assistant & RAG Query"):
            with gr.Row():
                with gr.Column(scale=5):
                    question_in = gr.Textbox(
                        label="Enter SEBI Compliance Question",
                        placeholder="e.g. What is the mandatory disclosure threshold for promoter insider trading under SEBI PIT?",
                        lines=3,
                    )
                    with gr.Row():
                        embedding_model_q = gr.Dropdown(
                            MODEL_CHOICES, value=DEFAULT_EMBEDDING_MODEL, label="Embedding Model"
                        )
                        answer_model_in = gr.Dropdown(
                            list(ANSWER_MODELS.keys()),
                            value=DEFAULT_ANSWER_MODEL,
                            label="LLM Answer Generator",
                        )
                    with gr.Row():
                        top_k_in = gr.Slider(1, 10, value=4, step=1, label="Top K Chunks")
                        hybrid_weight_in = gr.Slider(
                            0.0, 1.0, value=0.5, step=0.05,
                            label="Hybrid Weight (1 = Dense Vector, 0 = Keyword/BM25)",
                        )
                    query_btn = gr.Button("Search & Generate Compliance Answer", variant="primary")
                
                with gr.Column(scale=7):
                    timing_out = gr.Markdown()
                    answer_out = gr.Markdown(label="Grounded Compliance Response")
                    chunks_out = gr.Markdown(label="Retrieved Regulatory Source Chunks")

            query_btn.click(
                do_query,
                inputs=[
                    question_in,
                    embedding_model_q,
                    top_k_in,
                    hybrid_weight_in,
                    answer_model_in,
                ],
                outputs=[chunks_out, answer_out, timing_out],
            )

        with gr.Tab("2. Live Benchmark Head-to-Head Comparison"):
            gr.Markdown(
                "## 50-Question SEBI Benchmark Explorer\n"
                "Select any of the 50 benchmark questions across Tiers 1–5 to compare **Base LLM Performance vs. RAG System** live!"
            )
            with gr.Row():
                question_dropdown = gr.Dropdown(
                    choices=QUESTION_CHOICES,
                    value=QUESTION_CHOICES[0] if QUESTION_CHOICES else None,
                    label="Select Benchmark Question from 50-Question Dataset",
                )
                eval_model_choice = gr.Dropdown(
                    choices=list(ANSWER_MODELS.keys()),
                    value=DEFAULT_ANSWER_MODEL,
                    label="LLM Model to Compare",
                )
            
            with gr.Row():
                q_header_md = gr.Markdown()
            with gr.Row():
                q_expected_md = gr.Markdown()
                q_trap_md = gr.Markdown()

            compare_btn = gr.Button("Run Head-to-Head Comparison (Base LLM vs RAG)", variant="primary")
            
            with gr.Row():
                base_llm_out = gr.Markdown(label="Base LLM Response (Un-augmented)")
                rag_llm_out = gr.Markdown(label="RAG System Response (Ground-truth Augmented)")

            question_dropdown.change(
                load_benchmark_detail,
                inputs=[question_dropdown],
                outputs=[q_header_md, q_expected_md, q_trap_md, question_in],
            )
            demo.load(
                load_benchmark_detail,
                inputs=[question_dropdown],
                outputs=[q_header_md, q_expected_md, q_trap_md, question_in],
            )
            compare_btn.click(
                run_benchmark_head_to_head,
                inputs=[question_in, eval_model_choice],
                outputs=[base_llm_out, rag_llm_out],
            )

        with gr.Tab("3. Knowledge Base & Document Lab"):
            with gr.Row():
                with gr.Column():
                    file_in = gr.File(label="Upload Primary Regulatory Text (.pdf, .docx, .txt)")
                    embedding_model_in = gr.Dropdown(
                        MODEL_CHOICES, value=DEFAULT_EMBEDDING_MODEL, label="Embedding model"
                    )
                    chunk_size_in = gr.Slider(100, 3000, value=800, step=50, label="Chunk size (chars)")
                    chunk_overlap_in = gr.Slider(0, 500, value=100, step=10, label="Chunk overlap (chars)")
                    ingest_btn = gr.Button("Ingest Document into ChromaDB", variant="primary")
                    reset_btn = gr.Button("Clear All Ingested Documents")
                with gr.Column():
                    ingest_status = gr.Markdown()
                    docs_table = gr.Dataframe(
                        headers=["filename", "document_id", "num_chunks"],
                        label="Ingested SEBI Regulations (Active Collection)",
                    )

            ingest_btn.click(
                do_ingest,
                inputs=[file_in, embedding_model_in, chunk_size_in, chunk_overlap_in],
                outputs=[ingest_status, docs_table],
            )
            reset_btn.click(do_reset, inputs=[embedding_model_in], outputs=[ingest_status, docs_table])
            embedding_model_in.change(refresh_documents, inputs=[embedding_model_in], outputs=[docs_table])
            demo.load(refresh_documents, inputs=[embedding_model_in], outputs=[docs_table])

    demo.queue()
    return gr.mount_gradio_app(app, demo, path="/")
