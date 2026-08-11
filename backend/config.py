from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
UPLOAD_DIR = DATA_DIR / "uploads"
CHROMA_DIR = DATA_DIR / "chroma"

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
CHROMA_DIR.mkdir(parents=True, exist_ok=True)

# Embedding models students can pick between. Each gets its own Chroma
# collection since dimensions/semantics differ across models.
EMBEDDING_MODELS = {
    "MiniLM-L6 (fast, 384d)": "sentence-transformers/all-MiniLM-L6-v2",
    "MPNet-base (balanced, 768d)": "sentence-transformers/all-mpnet-base-v2",
    "BGE-small (retrieval-tuned, 384d)": "BAAI/bge-small-en-v1.5",
}
DEFAULT_EMBEDDING_MODEL = "MiniLM-L6 (fast, 384d)"

# LLMs students can pick between for answer synthesis. Together AI exposes an
# OpenAI-compatible endpoint, so both providers use the same client with a
# different base_url/api_key.
ANSWER_MODELS = {
    "gpt-5-nano (OpenAI)": {
        "provider": "openai",
        "model": "gpt-5-nano",
        "api_key_env": "OPENAI_API_KEY",
        "base_url": None,
    },
    "gpt-oss-20b (Together AI)": {
        "provider": "together",
        "model": "openai/gpt-oss-20b",
        "api_key_env": "TOGETHER_API_KEY",
        "base_url": "https://api.together.xyz/v1",
    },
    "gemma-3n-E4B-it (Together AI)": {
        "provider": "together",
        "model": "google/gemma-3n-E4B-it",
        "api_key_env": "TOGETHER_API_KEY",
        "base_url": "https://api.together.xyz/v1",
    },
}
DEFAULT_ANSWER_MODEL = "gpt-5-nano (OpenAI)"
