import re
import uuid

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

from backend.config import CHROMA_DIR, EMBEDDING_MODELS
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
        return []

    # Keyword scoring (BM25) needs the whole corpus for its IDF stats, and
    # embedding similarity needs the whole corpus too so a strong keyword
    # match isn't excluded just because it ranked outside the semantic
    # top-k. Fetch everything, score both ways, then blend per chunk.
    result = collection.query(
        query_texts=[question],
        n_results=count,
        include=["documents", "metadatas", "distances"],
    )

    docs = result["documents"][0]
    metas = result["metadatas"][0]
    distances = result["distances"][0]
    # cosine distance -> similarity score in [0, 1] (roughly)
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
    """Min-max scale to [0, 1] so keyword and embedding scores are comparable."""
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
    """Blend normalized embedding similarity and BM25 keyword scores.

    hybrid_weight slides the balance between the two: 1.0 = pure embedding,
    0.0 = pure keyword."""
    keyword_scores = BM25(docs).scores(question)
    sem_norm = _normalize(embedding_scores)
    kw_norm = _normalize(keyword_scores)
    return [
        hybrid_weight * sem + (1 - hybrid_weight) * kw
        for sem, kw in zip(sem_norm, kw_norm)
    ]


def new_document_id() -> str:
    return uuid.uuid4().hex[:12]
