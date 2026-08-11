from pydantic import BaseModel, Field


class IngestResponse(BaseModel):
    document_id: str
    filename: str
    num_chunks: int
    embedding_model: str
    chunk_size: int
    chunk_overlap: int


class DocumentInfo(BaseModel):
    document_id: str
    filename: str
    num_chunks: int
    embedding_model: str


class RetrievedChunk(BaseModel):
    document_id: str
    filename: str
    chunk_index: int
    text: str
    score: float


class QueryRequest(BaseModel):
    question: str
    embedding_model: str
    top_k: int = Field(default=4, ge=1, le=20)
    hybrid_weight: float = Field(default=0.5, ge=0.0, le=1.0)
    answer_model: str | None = None


class QueryResponse(BaseModel):
    chunks: list[RetrievedChunk]
    retrieval_latency_ms: float
    answer: str | None = None
    generation_latency_ms: float | None = None
