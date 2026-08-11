"""FastAPI Backend Entrypoint with Embedded Gradio App.

Allows running directly via `python3 -m backend.main` or `python backend/main.py`
to launch and expose the web application on http://localhost:7860/
"""
import os
import time
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from pydantic import BaseModel

load_dotenv()

from backend import generate, ingest, vectorstore
from backend.chunking import split_text
from backend.config import DEFAULT_ANSWER_MODEL, DEFAULT_EMBEDDING_MODEL

app = FastAPI(title="SEBI & Capital Markets Compliance AI", version="1.0")


class ChunkResponse(BaseModel):
    document_id: str
    filename: str
    chunk_index: int
    text: str
    score: float


class QueryRequest(BaseModel):
    question: str
    embedding_model: str = DEFAULT_EMBEDDING_MODEL
    top_k: int = 4
    hybrid_weight: float = 0.5
    answer_model: str = DEFAULT_ANSWER_MODEL


class QueryResponse(BaseModel):
    chunks: list[ChunkResponse]
    retrieval_latency_ms: float
    answer: str = ""
    generation_latency_ms: float = 0.0


@app.get("/api/health")
def health():
    return {"status": "ok", "app": "SEBI Compliance AI"}


@app.post("/api/ingest")
async def api_ingest(
    file: UploadFile = File(...),
    embedding_model: str = Form(DEFAULT_EMBEDDING_MODEL),
    chunk_size: int = Form(800),
    chunk_overlap: int = Form(100),
):
    contents = await file.read()
    text = ingest.extract_text(file.filename, contents)
    if not text.strip():
        raise HTTPException(400, "No extractable text found in uploaded file.")

    chunks = split_text(text, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    if not chunks:
        raise HTTPException(400, "Chunking produced 0 chunks.")

    doc_id = vectorstore.new_document_id()
    vectorstore.add_chunks(embedding_model, doc_id, file.filename, chunks)

    return {
        "filename": file.filename,
        "document_id": doc_id,
        "num_chunks": len(chunks),
        "embedding_model": embedding_model,
    }


@app.get("/api/documents")
def api_documents(embedding_model: str = DEFAULT_EMBEDDING_MODEL):
    return vectorstore.list_documents(embedding_model)


@app.post("/api/query", response_model=QueryResponse)
def api_query(req: QueryRequest):
    t0 = time.perf_counter()
    raw_chunks = vectorstore.query(
        req.embedding_model, req.question, req.top_k, req.hybrid_weight
    )
    retrieval_ms = (time.perf_counter() - t0) * 1000

    chunks = [
        ChunkResponse(
            document_id=c["document_id"],
            filename=c["filename"],
            chunk_index=c["chunk_index"],
            text=c["text"],
            score=c["score"],
        )
        for c in raw_chunks
    ]

    answer = ""
    generation_ms = 0.0
    if req.answer_model and req.answer_model != "None (retrieval only)":
        if not generate.is_configured(req.answer_model):
            raise HTTPException(400, f"API key for model '{req.answer_model}' not configured in environment.")
        t1 = time.perf_counter()
        answer = generate.generate_answer(req.question, [c.text for c in chunks], req.answer_model)
        generation_ms = (time.perf_counter() - t1) * 1000

    return QueryResponse(
        chunks=chunks,
        retrieval_latency_ms=retrieval_ms,
        answer=answer,
        generation_latency_ms=generation_ms,
    )


# Mount the Gradio UI at the root path
from ui.gradio_app import build_ui  # noqa: E402

build_ui(app)


if __name__ == "__main__":
    import uvicorn

    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 7860))
    print(f"\n=======================================================")
    print(f" Starting SEBI Compliance AI Web Server")
    print(f" Local URL:   http://127.0.0.1:{port}/")
    print(f" Network URL: http://{host}:{port}/")
    print(f"=======================================================\n", flush=True)
    uvicorn.run(app, host=host, port=port)
