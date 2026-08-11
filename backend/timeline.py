"""Interactive Statutory Compliance Timeline & Risk Heatmap Generator.

Parses regulatory compliance answers and generates:
1. Risk Severity Badge & Severity Score (CRITICAL / HIGH / MODERATE / STANDARD)
2. Chronological Compliance Event Timeline (T+0, T+2 Days, T+48 Hours, T+6 Months, etc.)
3. Interactive HTML Visualization for UI display
"""
import re
from typing import TypedDict


class TimelineEvent(TypedDict):
    step: str
    timing: str
    action: str
    badge_color: str


class TimelineResult(TypedDict):
    risk_level: str  # 'CRITICAL', 'HIGH', 'MODERATE', 'STANDARD'
    risk_color: str
    risk_description: str
    events: list[TimelineEvent]
    timeline_html: str


TIMEFRAME_PATTERNS = [
    (r"30\s*minutes", "T+30 Mins", "Stock Exchange Board Outcome Disclosure", "#ea4335"),
    (r"2\s*trading\s*days|two\s*trading\s*days", "T+2 Days", "Mandatory Promoter / KMP Trade Disclosure", "#fbbc04"),
    (r"48\s*hours", "T+48 Hours", "Trading Window Closure / Financial Disclosures", "#fbbc04"),
    (r"5\s*working\s*days|five\s*working\s*days", "T+5 Days", "FPI Divestment / Detailed Public Statement", "#34a853"),
    (r"7\s*working\s*days|seven\s*working\s*days", "T+7 Days", "Promoter Encumbrance / Pledge Disclosure", "#34a853"),
    (r"10\s*working\s*days", "T+10 Days", "Max Mutual Fund Redemption Suspension", "#4285f4"),
    (r"45\s*days", "T+45 Days", "Quarterly Unaudited Financial Submission", "#4285f4"),
    (r"6\s*months|six\s*months", "T+6 Months", "Contra-Trade Restrictions / Promoter Lock-In", "#ea4335"),
    (r"18\s*months", "T+18 Months", "Minimum Promoter Contribution IPO Lock-In", "#4285f4"),
    (r"3\s*years|three\s*years", "T+3 Years", "Cooling-Off Period for Independent Directors", "#4285f4"),
]


def extract_timeline_and_risk(response_text: str, question_text: str = "") -> TimelineResult:
    """Analyze compliance response text and extract chronological timeline & risk level."""
    combined = f"{question_text} {response_text}".lower()

    # Determine Risk Severity
    if any(k in combined for k in ["insider trading", "contra trade", "upsi", "open offer trigger", "penalty"]):
        risk_level = "CRITICAL COMPLIANCE REGIME"
        risk_color = "#d93025"
        risk_desc = "Strict Statutory Liability & Penalty Consequences under SEBI PIT / SAST Regulations"
    elif any(k in combined for k in ["material event", "disclosure", "pledge", "reclassification", "ter limit"]):
        risk_level = "HIGH MONITORING REQUIREMENT"
        risk_color = "#f2994a"
        risk_desc = "Mandatory Disclosure Deadlines & Statutory Filing Obligations"
    else:
        risk_level = "STANDARD REGULATORY COMPLIANCE"
        risk_color = "#27ae60"
        risk_desc = "Routine Disclosure & Operational Guidelines"

    events: list[TimelineEvent] = [
        {
            "step": "T+0 (Execution)",
            "timing": "Immediate",
            "action": "Transaction Trigger / Decision Initiated",
            "badge_color": "#1a73e8",
        }
    ]

    matched_timings = set()
    for pattern, tag, default_action, color in TIMEFRAME_PATTERNS:
        if re.search(pattern, response_text, re.IGNORECASE):
            if tag not in matched_timings:
                matched_timings.add(tag)

                # Extract context sentence for action
                sentences = re.split(r"(?<=[.!?])\s+", response_text)
                action_text = default_action
                for s in sentences:
                    if re.search(pattern, s, re.IGNORECASE):
                        action_text = s.strip()[:140] + ("..." if len(s.strip()) > 140 else "")
                        break

                events.append({
                    "step": tag,
                    "timing": tag,
                    "action": action_text,
                    "badge_color": color,
                })

    if len(events) == 1:
        events.append({
            "step": "Ongoing",
            "timing": "Continuous",
            "action": "Compliance Monitoring & SDD Database Audit Trail",
            "badge_color": "#34a853",
        })

    # Render Interactive Timeline HTML
    timeline_cards_html = []
    for i, ev in enumerate(events):
        card = (
            f'<div style="flex: 1; min-width: 180px; background: #ffffff; border-left: 4px solid {ev["badge_color"]}; '
            f'padding: 12px; margin: 6px; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">'
            f'<div style="font-size: 0.85em; font-weight: bold; color: {ev["badge_color"]}; uppercase;">{ev["step"]}</div>'
            f'<div style="font-size: 0.95em; color: #202124; margin-top: 4px;">{ev["action"]}</div>'
            f'</div>'
        )
        timeline_cards_html.append(card)

    html_out = (
        f'<div style="font-family: sans-serif; background: #f8f9fa; border: 1px solid #dadce0; border-radius: 8px; padding: 16px; margin-top: 12px;">'
        f'<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">'
        f'<div>'
        f'<span style="background-color: {risk_color}; color: #ffffff; font-weight: bold; padding: 4px 10px; border-radius: 12px; font-size: 0.85em;">'
        f'🚨 {risk_level}</span>'
        f'<div style="font-size: 0.85em; color: #5f6368; margin-top: 6px;">{risk_desc}</div>'
        f'</div>'
        f'<div style="font-size: 0.85em; color: #70757a; font-weight: bold;">Statutory Action Flow</div>'
        f'</div>'
        f'<div style="display: flex; flex-wrap: wrap; gap: 8px;">'
        f'{"".join(timeline_cards_html)}'
        f'</div>'
        f'</div>'
    )

    return {
        "risk_level": risk_level,
        "risk_color": risk_color,
        "risk_description": risk_desc,
        "events": events,
        "timeline_html": html_out,
    }
