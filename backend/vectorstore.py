import re
import uuid
from pathlib import Path

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

from backend.config import BASE_DIR, CHROMA_DIR, EMBEDDING_MODELS
from backend.keyword_search import BM25

_client = chromadb.PersistentClient(path=str(CHROMA_DIR))
_collection_cache: dict[str, "chromadb.Collection"] = {}


def _collection_name(embedding_model_label: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", embedding_model_label).strip("_").lower()
    return f"rag_{slug}"


def get_collection(embedding_model_label: str):
    if embedding_model_label not in _collection_cache:
        model_name = EMBEDDING_MODELS[embedding_model_label]
        embed_fn = SentenceTransformerEmbeddingFunction(model_name=model_name)
        _collection_cache[embedding_model_label] = _client.get_or_create_collection(
            name=_collection_name(embedding_model_label),
            embedding_function=embed_fn,
            metadata={"hnsw:space": "cosine"},
        )
    return _collection_cache[embedding_model_label]


def _auto_populate_if_empty(embedding_model_label: str) -> None:
    """Auto-populates vectorstore from data/sebi_documents/ if ChromaDB is empty on Linux/Unix."""
    docs_dir = BASE_DIR / "data" / "sebi_documents"
    text_files = list(docs_dir.glob("*.txt")) if docs_dir.exists() else []

    if not text_files:
        try:
            from scripts import download_sebi_documents_comprehensive
            download_sebi_documents_comprehensive.main()
            return
        except Exception:
            pass

    from backend import ingest
    from backend.chunking import split_text

    print(f"\n⚡ Auto-ingesting SEBI statutory documents into empty collection ({embedding_model_label})...", flush=True)
    for tf in text_files:
        try:
            with open(tf, "rb") as f:
                raw = f.read()
            text = ingest.extract_text(tf.name, raw)
            if text.strip():
                chunks = split_text(text, chunk_size=800, chunk_overlap=100)
                if chunks:
                    doc_id = new_document_id()
                    add_chunks(embedding_model_label, doc_id, tf.name, chunks)
        except Exception as e:
            print(f"Error auto-ingesting {tf.name}: {e}", flush=True)
    print("✅ Auto-ingestion complete!\n", flush=True)


def add_chunks(
    embedding_model_label: str,
    document_id: str,
    filename: str,
    chunks: list[str],
) -> None:
    collection = get_collection(embedding_model_label)
    ids = [f"{document_id}_{i}" for i in range(len(chunks))]
    metadatas = [
        {"document_id": document_id, "filename": filename, "chunk_index": i}
        for i in range(len(chunks))
    ]
    collection.add(ids=ids, documents=chunks, metadatas=metadatas)


def list_documents(embedding_model_label: str) -> list[dict]:
    collection = get_collection(embedding_model_label)
    if collection.count() == 0:
        _auto_populate_if_empty(embedding_model_label)

    result = collection.get(include=["metadatas"])
    docs: dict[str, dict] = {}
    for meta in result["metadatas"]:
        doc_id = meta["document_id"]
        if doc_id not in docs:
            docs[doc_id] = {
                "document_id": doc_id,
                "filename": meta["filename"],
                "num_chunks": 0,
            }
        docs[doc_id]["num_chunks"] += 1
    return list(docs.values())


def delete_document(embedding_model_label: str, document_id: str) -> None:
    collection = get_collection(embedding_model_label)
    collection.delete(where={"document_id": document_id})


def reset_collection(embedding_model_label: str) -> None:
    collection = get_collection(embedding_model_label)
    all_ids = collection.get(include=[])["ids"]
    if all_ids:
        collection.delete(ids=all_ids)


def query(
    embedding_model_label: str,
    question: str,
    top_k: int,
    hybrid_weight: float = 0.5,
) -> list[dict]:
    collection = get_collection(embedding_model_label)
    count = collection.count()
    if count == 0:
        _auto_populate_if_empty(embedding_model_label)
        count = collection.count()
        if count == 0:
            return []

    result = collection.query(
        query_texts=[question],
        n_results=count,
        include=["documents", "metadatas", "distances"],
    )

    docs = result["documents"][0]
    metas = result["metadatas"][0]
    distances = result["distances"][0]
    embedding_scores = [1 - d / 2 for d in distances]

    scores = _hybrid_scores(docs, embedding_scores, question, hybrid_weight)
    order = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]

    return [
        {
            "document_id": metas[i]["document_id"],
            "filename": metas[i]["filename"],
            "chunk_index": metas[i]["chunk_index"],
            "text": docs[i],
            "score": scores[i],
        }
        for i in order
    ]


def _normalize(scores: list[float]) -> list[float]:
    if not scores:
        return scores
    lo, hi = min(scores), max(scores)
    if hi - lo < 1e-10:
        return [1.0 if hi > 0 else 0.0] * len(scores)
    return [(s - lo) / (hi - lo) for s in scores]


def _hybrid_scores(
    docs: list[str],
    embedding_scores: list[float],
    question: str,
    hybrid_weight: float,
) -> list[float]:
    keyword_scores = BM25(docs).scores(question)
    sem_norm = _normalize(embedding_scores)
    kw_norm = _normalize(keyword_scores)
    return [
        hybrid_weight * sem + (1 - hybrid_weight) * kw
        for sem, kw in zip(sem_norm, kw_norm)
    ]


def new_document_id() -> str:
    return uuid.uuid4().hex[:12]
