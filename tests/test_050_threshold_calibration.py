import unittest

from treasury_liquidity_map.models import Record
from treasury_liquidity_map.scoring import score_record


class DepthCheck50(unittest.TestCase):
    def test_050_threshold_calibration(self):
        record = Record(id="cashflow-050", exposure=65412, signal=0.253, urgency=8)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
