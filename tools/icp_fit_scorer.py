"""
icp_fit_scorer.py - Evaluates enterprise company size and revenue against Ideal Customer Profile tiers
"""
import sys
import json


def score_icp_fit(firmographics_json: str):
    import json
    data = json.loads(firmographics_json) if isinstance(firmographics_json, str) else firmographics_json
    emp = data.get("employee_count", 500)
    rev = data.get("annual_revenue_usd", 50000000.0)
    tier = "TIER_1_ICP" if emp >= 250 and rev >= 25000000.0 else "TIER_2_ICP"
    return {"icp_tier": tier, "status": tier}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "icp-fit-scorer"}))
