#!/usr/bin/env python3
"""Classify email priority based on sender, subject keywords, and age."""
import json, sys

URGENT_KEYWORDS = ["urgent", "asap", "critical", "outage", "down", "blocked", "deadline"]
VIP_DOMAINS = ["ceo", "cto", "vp", "director", "board"]

def classify(data):
    subject = data.get("subject", "").lower()
    sender = data.get("sender", "").lower()
    age_hours = data.get("age_hours", 0)
    has_attachment = data.get("has_attachment", False)

    score = 0
    reasons = []
    if any(kw in subject for kw in URGENT_KEYWORDS):
        score += 3
        reasons.append("urgent keyword in subject")
    if any(vip in sender for vip in VIP_DOMAINS):
        score += 2
        reasons.append("VIP sender")
    if age_hours > 24:
        score += 1
        reasons.append("unanswered >24h")

    priority = "high" if score >= 3 else "medium" if score >= 1 else "low"
    return {"priority": priority, "score": score, "reasons": reasons}

if __name__ == "__main__":
    print(json.dumps(classify(json.loads(sys.argv[1])), indent=2))
