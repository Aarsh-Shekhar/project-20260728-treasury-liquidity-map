import unittest

from treasury_liquidity_map.models import Record
from treasury_liquidity_map.scoring import score_record


class DepthCheck38(unittest.TestCase):
    def test_038_field_validation(self):
        record = Record(id="cashflow-038", exposure=75374, signal=0.412, urgency=6)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
