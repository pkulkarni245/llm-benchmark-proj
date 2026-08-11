"""Multi-Model 'LLM Jury' Consensus Engine.

Queries all 3 models (gpt-5-nano, gpt-oss-20b, gemma-3n) concurrently,
evaluates cross-model agreement, and highlights consensus vs divergence areas.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import TypedDict

from backend import generate


class ModelJuryOpinion(TypedDict):
    model_key: str
    model_name: str
    response: str
    char_count: int


class JuryConsensusResult(TypedDict):
    consensus_status: str  # 'UNANIMOUS CONSENSUS (100%)', 'MAJORITY CONSENSUS (66%)', 'SPLIT DECISION'
    consensus_score: float
    opinions: list[ModelJuryOpinion]
    consensus_html: str


def run_llm_jury_consensus(question_text: str, context_chunks: list[str]) -> JuryConsensusResult:
    """Run all 3 models in parallel and evaluate cross-model consensus."""
    models = [
        ("gpt-5-nano", "gpt-5-nano (OpenAI)"),
        ("gpt-oss-20b", "gpt-oss-20b (Together AI)"),
        ("gemma-3n", "gemma-3n-E4B-it (Together AI)"),
    ]

    def _call(m_key, m_label):
        try:
            if context_chunks:
                resp = generate.generate_answer(question_text, context_chunks, m_label)
            else:
                resp = generate.generate_raw(question_text, m_label)
            return m_key, m_label, resp
        except Exception as e:
            return m_key, m_label, f"ERROR: {str(e)}"

    opinions: list[ModelJuryOpinion] = []
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(_call, k, l) for k, l in models]
        for f in as_completed(futures):
            m_key, m_label, resp = f.result()
            opinions.append({
                "model_key": m_key,
                "model_name": m_label,
                "response": resp,
                "char_count": len(resp),
            })

    # Sort in standard order
    opinions.sort(key=lambda x: x["model_key"])

    # Determine Consensus Status
    # Inspect numerical keywords across responses
    resp_texts = [op["response"].lower() for op in opinions]

    nums_0 = set(re.findall(r"\b\d+\b", resp_texts[0])) if len(resp_texts) > 0 else set()
    nums_1 = set(re.findall(r"\b\d+\b", resp_texts[1])) if len(resp_texts) > 1 else set()
    nums_2 = set(re.findall(r"\b\d+\b", resp_texts[2])) if len(resp_texts) > 2 else set()

    shared_all = nums_0.intersection(nums_1).intersection(nums_2)

    if shared_all:
        consensus_status = "UNANIMOUS CONSENSUS (100% Agreement on Key Numbers)"
        consensus_score = 100.0
        badge_color = "#137333"
        bg_color = "#e6f4ea"
    elif len(nums_0.intersection(nums_1)) > 0 or len(nums_1.intersection(nums_2)) > 0 or len(nums_0.intersection(nums_2)) > 0:
        consensus_status = "MAJORITY CONSENSUS (66% Model Agreement)"
        consensus_score = 66.7
        badge_color = "#b06000"
        bg_color = "#fef7e0"
    else:
        consensus_status = "SPLIT DECISION (Subtle Model Divergence)"
        consensus_score = 33.3
        badge_color = "#c5221f"
        bg_color = "#fce8e6"

    # Render Side-by-Side Jury HTML
    columns_html = []
    for op in opinions:
        col = (
            f'<div style="flex: 1; min-width: 260px; background: #ffffff; border: 1px solid #dadce0; '
            f'border-radius: 8px; padding: 14px; margin: 4px;">'
            f'<div style="font-weight: bold; color: #1a73e8; margin-bottom: 8px; border-bottom: 2px solid #e8eaed; padding-bottom: 4px;">'
            f'⚖️ {op["model_name"]}'
            f'</div>'
            f'<div style="font-size: 0.9em; color: #3c4043; line-height: 1.6; max-height: 280px; overflow-y: auto;">'
            f'{op["response"].replace("\n", "<br>")}'
            f'</div>'
            f'</div>'
        )
        columns_html.append(col)

    html_out = (
        f'<div style="font-family: sans-serif; margin-top: 14px;">'
        f'<div style="background: {bg_color}; border: 1px solid {badge_color}; border-radius: 8px; padding: 12px; margin-bottom: 12px; font-weight: bold; color: {badge_color};">'
        f'👨‍⚖️ LLM Jury Verdict: {consensus_status} (Score: {consensus_score:.1f}%)'
        f'</div>'
        f'<div style="display: flex; flex-wrap: wrap; gap: 8px;">'
        f'{"".join(columns_html)}'
        f'</div>'
        f'</div>'
    )

    return {
        "consensus_status": consensus_status,
        "consensus_score": consensus_score,
        "opinions": opinions,
        "consensus_html": html_out,
    }
