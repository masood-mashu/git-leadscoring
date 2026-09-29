"""
sdr_routing_engine.py - Assigns lead to specialized enterprise account executive or inbound SDR queue
"""
import sys
import json


def route_sales_lead(qualification_json: str):
    import json
    data = json.loads(qualification_json) if isinstance(qualification_json, str) else qualification_json
    tier = data.get("icp_tier", "TIER_1_ICP")
    route = "ENTERPRISE_AE" if tier == "TIER_1_ICP" else "INBOUND_SDR"
    return {"assigned_queue": route, "status": "ROUTED_TO_AE" if route == "ENTERPRISE_AE" else "ROUTED_TO_SDR"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "sdr-routing-engine"}))
