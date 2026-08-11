import time

from dotenv import load_dotenv
from fastapi import FastAPI, File, Form, HTTPException, UploadFile

load_dotenv()

from backend import generate, ingest, vectorstore
from backend.chunking import split_text
from backend.config import (
    ANSWER_MODELS,
    DEFAULT_ANSWER_MODEL,
    DEFAULT_EMBEDDING_MODEL,
    EMBEDDING_MODELS,
)
from backend.schemas import (
    DocumentInfo,
    IngestResponse,
    QueryRequest,
    QueryResponse,
    RetrievedChunk,
)

app = FastAPI(title="RAG Skeleton")


@app.get("/embedding-models")
def embedding_models() -> dict:
    return {"models": list(EMBEDDING_MODELS.keys()), "default": DEFAULT_EMBEDDING_MODEL}


@app.get("/answer-models")
def answer_models() -> dict:
    return {
        "models": list(ANSWER_MODELS.keys()),
        "default": DEFAULT_ANSWER_MODEL,
        "available": {label: generate.is_configured(label) for label in ANSWER_MODELS},
    }


@app.post("/documents", response_model=IngestResponse)
async def upload_document(
    file: UploadFile = File(...),
    embedding_model: str = Form(DEFAULT_EMBEDDING_MODEL),
    chunk_size: int = Form(800),
    chunk_overlap: int = Form(100),
):
    if embedding_model not in EMBEDDING_MODELS:
        raise HTTPException(400, f"Unknown embedding model: {embedding_model}")

    raw = await file.read()
    text = ingest.extract_text(file.filename, raw)
    if not text.strip():
        raise HTTPException(400, "No extractable text found in file")

    chunks = split_text(text, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    if not chunks:
        raise HTTPException(400, "Chunking produced no chunks")

    document_id = vectorstore.new_document_id()
    vectorstore.add_chunks(embedding_model, document_id, file.filename, chunks)

    return IngestResponse(
        document_id=document_id,
        filename=file.filename,
        num_chunks=len(chunks),
        embedding_model=embedding_model,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )


@app.get("/documents", response_model=list[DocumentInfo])
def get_documents(embedding_model: str = DEFAULT_EMBEDDING_MODEL):
    docs = vectorstore.list_documents(embedding_model)
    return [DocumentInfo(embedding_model=embedding_model, **d) for d in docs]


@app.delete("/documents/{document_id}")
def delete_document(document_id: str, embedding_model: str = DEFAULT_EMBEDDING_MODEL):
    vectorstore.delete_document(embedding_model, document_id)
    return {"deleted": document_id}


@app.post("/reset")
def reset(embedding_model: str = DEFAULT_EMBEDDING_MODEL):
    vectorstore.reset_collection(embedding_model)
    return {"reset": embedding_model}


@app.post("/query", response_model=QueryResponse)
def run_query(req: QueryRequest):
    if req.embedding_model not in EMBEDDING_MODELS:
        raise HTTPException(400, f"Unknown embedding model: {req.embedding_model}")

    t0 = time.perf_counter()
    raw_chunks = vectorstore.query(
        req.embedding_model, req.question, req.top_k, req.hybrid_weight
    )
    retrieval_ms = (time.perf_counter() - t0) * 1000

    chunks = [RetrievedChunk(**c) for c in raw_chunks]

    answer, generation_ms = None, None
    if req.answer_model:
        if req.answer_model not in ANSWER_MODELS:
            raise HTTPException(400, f"Unknown answer model: {req.answer_model}")
        if not generate.is_configured(req.answer_model):
            raise HTTPException(400, f"No API key configured for {req.answer_model}")
        t1 = time.perf_counter()
        answer = generate.generate_answer(req.question, [c.text for c in chunks], req.answer_model)
        generation_ms = (time.perf_counter() - t1) * 1000

    return QueryResponse(
        chunks=chunks,
        retrieval_latency_ms=retrieval_ms,
        answer=answer,
        generation_latency_ms=generation_ms,
    )


# Mount the Gradio UI at the root path, in the same process.
from ui.gradio_app import build_ui  # noqa: E402

build_ui(app)
