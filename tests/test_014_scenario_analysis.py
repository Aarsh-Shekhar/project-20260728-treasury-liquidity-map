import unittest

from treasury_liquidity_map.models import Record
from treasury_liquidity_map.scoring import score_record


class DepthCheck14(unittest.TestCase):
    def test_014_scenario_analysis(self):
        record = Record(id="cashflow-014", exposure=81721, signal=0.536, urgency=7)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
