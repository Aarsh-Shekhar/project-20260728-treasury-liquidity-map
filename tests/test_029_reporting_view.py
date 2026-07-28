import unittest

from treasury_liquidity_map.models import Record
from treasury_liquidity_map.scoring import score_record


class DepthCheck29(unittest.TestCase):
    def test_029_reporting_view(self):
        record = Record(id="cashflow-029", exposure=54184, signal=0.645, urgency=5)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
