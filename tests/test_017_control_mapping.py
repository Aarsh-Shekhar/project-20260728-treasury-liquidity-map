import unittest

from treasury_liquidity_map.models import Record
from treasury_liquidity_map.scoring import score_record


class DepthCheck17(unittest.TestCase):
    def test_017_control_mapping(self):
        record = Record(id="cashflow-017", exposure=6380, signal=0.850, urgency=6)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
