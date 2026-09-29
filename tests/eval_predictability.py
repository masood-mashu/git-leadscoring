"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitLeadScoring.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.icp_fit_scorer import *
from tools.behavioral_intent_classifier import *
from tools.sdr_routing_engine import *

class TestGitLeadScoringPredictability(unittest.TestCase):
    def test_icp_fit_scorer(self):
        res = score_icp_fit('{"employee_count": 500, "annual_revenue_usd": 60000000.0}')
        self.assertEqual(res["icp_tier"], "TIER_1_ICP")
        self.assertEqual(res["status"], "TIER_1_ICP")

    def test_behavioral_intent_classifier(self):
        res = classify_behavioral_intent('{"pricing_page_views": 3, "whitepaper_downloads": 1}')
        self.assertGreaterEqual(res["intent_score"], 40)
        self.assertEqual(res["status"], "HIGH_INTENT")

    def test_sdr_routing_engine(self):
        res = route_sales_lead('{"icp_tier": "TIER_1_ICP"}')
        self.assertEqual(res["assigned_queue"], "ENTERPRISE_AE")
        self.assertEqual(res["status"], "ROUTED_TO_AE")


if __name__ == "__main__":
    unittest.main()
