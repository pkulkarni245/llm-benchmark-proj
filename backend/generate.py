import os
import sys
from openai import OpenAI

from backend.config import ANSWER_MODELS

_clients: dict[str, OpenAI] = {}

# Fallback models in case template placeholder model names return API errors
FALLBACK_MODELS = {
    "openai": ["gpt-4o-mini", "gpt-3.5-turbo", "gpt-4o"],
    "together": [
        "mistralai/Mistral-7B-Instruct-v0.1",
        "Qwen/Qwen2.5-7B-Instruct-Turbo",
        "meta-llama/Llama-3-8b-chat-hf",
    ],
}


def is_configured(answer_model_label: str) -> bool:
    spec = ANSWER_MODELS.get(answer_model_label)
    return bool(spec and os.environ.get(spec["api_key_env"]))


def _get_client(answer_model_label: str) -> OpenAI:
    if answer_model_label not in _clients:
        spec = ANSWER_MODELS[answer_model_label]
        api_key = os.environ[spec["api_key_env"]]
        _clients[answer_model_label] = OpenAI(api_key=api_key, base_url=spec["base_url"])
    return _clients[answer_model_label]


def _call_completion(answer_model_label: str, messages: list[dict]) -> str:
    client = _get_client(answer_model_label)
    spec = ANSWER_MODELS[answer_model_label]
    primary_model = spec["model"]
    provider = spec.get("provider", "openai")

    models_to_try = [primary_model] + FALLBACK_MODELS.get(provider, [])

    last_err = None
    for m in models_to_try:
        try:
            response = client.chat.completions.create(
                model=m,
                messages=messages,
            )
            return response.choices[0].message.content
        except Exception as e:
            last_err = e
            continue

    raise RuntimeError(f"Failed to generate response across models {models_to_try}: {str(last_err)}")


def generate_raw(prompt: str, answer_model_label: str) -> str:
    """Send a prompt straight to the model, with no RAG context wrapping."""
    messages = [{"role": "user", "content": prompt}]
    return _call_completion(answer_model_label, messages)


def generate_answer(question: str, chunks: list[str], answer_model_label: str) -> str:
    """Synthesize an answer from retrieved chunks. This is the step
    students optimize retrieval parameters *for* - better chunks in,
    better grounded answer out."""
    context = "\n\n".join(f"[{i + 1}] {c}" for i, c in enumerate(chunks))
    prompt = (
        "Answer the question using only the context below. If the context "
        "doesn't contain the answer, say so explicitly. Cite sources inline "
        "like [1], [2].\n\n"
        f"Context:\n{context}\n\nQuestion: {question}"
    )
    messages = [{"role": "user", "content": prompt}]
    return _call_completion(answer_model_label, messages)
