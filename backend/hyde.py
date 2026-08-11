"""HyDE (Hypothetical Document Embeddings) Advanced Query Rewriter.

Generates a hypothetical statutory legal provision first, then embeds the
hypothetical text to retrieve higher-precision chunks from ChromaDB.
"""
from typing import TypedDict

from backend import generate, vectorstore
from backend.config import DEFAULT_EMBEDDING_MODEL


class HyDEResult(TypedDict):
    original_query: str
    hypothetical_document: str
    retrieved_chunks: list[dict]
    final_answer: str
    hyde_html: str


def run_hyde_rag_pipeline(query_text: str, model_label: str = "gpt-5-nano (OpenAI)") -> HyDEResult:
    """Execute HyDE RAG pipeline: Hypothetical Document Generation -> Vector Retrieval -> Final Grounded Synthesis."""
    hyde_prompt = (
        "Write a hypothetical formal SEBI statutory legal section or circular clause "
        f"that directly answers the following legal query:\n\"{query_text}\"\n\n"
        "Write only the hypothetical legal text, with no introductory meta-commentary."
    )

    try:
        hypo_doc = generate.generate_raw(hyde_prompt, model_label)
    except Exception:
        hypo_doc = f"SEBI Statutory Regulation provision regarding {query_text}."

    # Retrieve chunks using hypothetical document text
    chunks = vectorstore.query(DEFAULT_EMBEDDING_MODEL, hypo_doc, top_k=4, hybrid_weight=0.5)
    chunk_texts = [c["text"] for c in chunks]

    # Synthesize final answer
    if chunk_texts:
        final_ans = generate.generate_answer(query_text, chunk_texts, model_label)
    else:
        final_ans = "HyDE RAG Notice: No relevant statutory documents found in Knowledge Base."

    # Render HyDE HTML Badge
    html_out = (
        f'<div style="font-family: sans-serif; background: #e8f0fe; border: 1px solid #1a73e8; border-radius: 8px; padding: 14px; margin-top: 10px;">'
        f'<div style="font-weight: bold; color: #1a73e8; margin-bottom: 6px;">🧠 HyDE Advanced Retrieval Activated</div>'
        f'<div style="font-size: 0.85em; color: #3c4043; margin-bottom: 8px;">'
        f'<b>Generated Hypothetical Legal Document:</b> <i>"{hypo_doc[:220]}..."</i>'
        f'</div>'
        f'<div style="font-size: 0.85em; color: #1e8e3e; font-weight: bold;">'
        f'-> Retrieved {len(chunks)} High-Precision Statutory Chunks'
        f'</div>'
        f'</div>'
    )

    return {
        "original_query": query_text,
        "hypothetical_document": hypo_doc,
        "retrieved_chunks": chunks,
        "final_answer": final_ans,
        "hyde_html": html_out,
    }
