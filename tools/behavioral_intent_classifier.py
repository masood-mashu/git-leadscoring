"""
behavioral_intent_classifier.py - Calculates composite buyer intent score from multi-touch website interactions
"""
import sys
import json


def classify_behavioral_intent(interactions_json: str):
    import json
    data = json.loads(interactions_json) if isinstance(interactions_json, str) else interactions_json
    score = (data.get("pricing_page_views", 0) * 20) + (data.get("whitepaper_downloads", 0) * 10) + (data.get("webinar_attended", False) * 25)
    is_high = score >= 40
    return {"intent_score": score, "status": "HIGH_INTENT" if is_high else "MODERATE_INTENT"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "behavioral-intent-classifier"}))
