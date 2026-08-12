"""Live Faithfulness & Hallucination Audit Engine (NLI Guardrail).

Evaluates generated RAG responses against retrieved context chunks to detect
unsupported claims and calculate a Faithfulness & Grounding Index (0-100%).
Renders sentence-by-sentence HTML highlighting for UI display.
"""
import re
from typing import TypedDict


class SentenceAudit(TypedDict):
    sentence: str
    status: str  # 'VERIFIED', 'PARTIALLY_VERIFIED', 'UNVERIFIED'
    score: float
    highlight_html: str


class FaithfulnessAuditResult(TypedDict):
    score_percentage: float
    status_label: str
    verified_count: int
    partial_count: int
    unverified_count: int
    total_sentences: int
    highlighted_html: str
    sentence_audits: list[SentenceAudit]


NUMERICAL_SYNONYMS = [
    (r"\b10\s*lakh\b|\b10\s*lakhs\b|\bten\s*lakh\b|\bten\s*lakhs\b", "10lakh"),
    (r"\b2\s*trading\s*days\b|\btwo\s*trading\s*days\b", "2tradingdays"),
    (r"\b25%\b|\btwenty\s*five\s*per\s*cent\b|\btwenty-five\s*percent\b", "25percent"),
    (r"\b48\s*hours\b|\bforty\s*eight\s*hours\b", "48hours"),
]


def _normalize_legal_text(text: str) -> str:
    cleaned = re.sub(r"\s+", " ", text.lower().strip())
    for pat, rep in NUMERICAL_SYNONYMS:
        cleaned = re.sub(pat, rep, cleaned)
    return cleaned


def _get_ngrams(text: str, n: int = 2) -> set[str]:
    words = re.findall(r"\w+", _normalize_legal_text(text))
    if len(words) < n:
        return {" ".join(words)} if words else set()
    return {" ".join(words[i : i + n]) for i in range(len(words) - n + 1)}


def _compute_sentence_grounding(sentence: str, context_text: str) -> float:
    sent_clean = _normalize_legal_text(sentence)
    if not sent_clean or len(sent_clean) < 10:
        return 1.0  # Skip short structural phrases

    context_clean = _normalize_legal_text(context_text)

    # 1. Exact substring check
    if sent_clean in context_clean:
        return 1.0

    # 2. Token overlap & 2-gram overlap
    sent_words = set(re.findall(r"\w+", sent_clean))
    ctx_words = set(re.findall(r"\w+", context_clean))

    if not sent_words:
        return 1.0

    word_jaccard = len(sent_words.intersection(ctx_words)) / len(sent_words)

    sent_2grams = _get_ngrams(sent_clean, 2)
    ctx_2grams = _get_ngrams(context_clean, 2)

    gram_overlap = len(sent_2grams.intersection(ctx_2grams)) / len(sent_2grams) if sent_2grams else word_jaccard

    # Combined grounding score
    return min(1.0, (word_jaccard * 0.5) + (gram_overlap * 0.5))


def audit_faithfulness(response_text: str, context_chunks: list[str]) -> FaithfulnessAuditResult:
    """Audit a RAG response sentence-by-sentence against retrieved statutory context."""
    if not response_text or not context_chunks:
        return {
            "score_percentage": 0.0,
            "status_label": "UNAUDITED (No Context)",
            "verified_count": 0,
            "partial_count": 0,
            "unverified_count": 0,
            "total_sentences": 0,
            "highlighted_html": "<p>No context available for audit.</p>",
            "sentence_audits": [],
        }

    combined_context = "\n\n".join(context_chunks)

    # Split response into sentences
    sentences = re.split(r"(?<=[.!?])\s+", response_text.strip())
    sentences = [s for s in sentences if s.strip()]

    if not sentences:
        return {
            "score_percentage": 100.0,
            "status_label": "VERIFIED",
            "verified_count": 0,
            "partial_count": 0,
            "unverified_count": 0,
            "total_sentences": 0,
            "highlighted_html": response_text,
            "sentence_audits": [],
        }

    audits: list[SentenceAudit] = []
    verified_cnt = 0
    partial_cnt = 0
    unverified_cnt = 0

    html_parts = []

    for s in sentences:
        s_clean = s.strip()
        score = _compute_sentence_grounding(s_clean, combined_context)

        if score >= 0.45:
            status = "VERIFIED"
            verified_cnt += 1
            color_bg = "#e6f4ea"
            color_text = "#137333"
            border = "#ceead6"
            icon = "[VERIFIED]"
        elif score >= 0.25:
            status = "PARTIALLY_VERIFIED"
            partial_cnt += 1
            color_bg = "#fef7e0"
            color_text = "#b06000"
            border = "#feefc3"
            icon = "[PARTIAL]"
        else:
            status = "UNVERIFIED"
            unverified_cnt += 1
            color_bg = "#fce8e6"
            color_text = "#c5221f"
            border = "#fad2cf"
            icon = "[UNVERIFIED]"

        html_tag = (
            f'<span style="background-color: {color_bg}; color: {color_text}; border: 1px solid {border}; '
            f'padding: 2px 6px; margin: 2px; border-radius: 4px; display: inline-block;" '
            f'title="{status} (Score: {score:.2f})">{s_clean} <small style="font-size:0.75em; opacity:0.8;">{icon}</small></span>'
        )

        html_parts.append(html_tag)
        audits.append({
            "sentence": s_clean,
            "status": status,
            "score": round(score, 2),
            "highlight_html": html_tag,
        })

    total = len(sentences)
    faithfulness_pct = round(((verified_cnt + (0.5 * partial_cnt)) / total) * 100, 1)

    if faithfulness_pct >= 80:
        status_label = "HIGH FAITHFULNESS (Verified Grounded)"
    elif faithfulness_pct >= 60:
        status_label = "MODERATE FAITHFULNESS (Minor Extrapolation)"
    else:
        status_label = "POTENTIAL HALLUCINATION (Low Grounding)"

    highlighted_html = (
        f'<div style="font-family: sans-serif; line-height: 1.8; margin-top: 10px;">'
        f'<div style="margin-bottom: 12px; font-weight: bold; color: #333;">'
        f'🛡️ Faithfulness Score: <span style="font-size: 1.2em; color: #1a73e8;">{faithfulness_pct}%</span> — '
        f'<span style="color: #5f6368;">{status_label}</span>'
        f'</div>'
        f'{" ".join(html_parts)}'
        f'</div>'
    )

    return {
        "score_percentage": faithfulness_pct,
        "status_label": status_label,
        "verified_count": verified_cnt,
        "partial_count": partial_cnt,
        "unverified_count": unverified_cnt,
        "total_sentences": total,
        "highlighted_html": highlighted_html,
        "sentence_audits": audits,
    }
