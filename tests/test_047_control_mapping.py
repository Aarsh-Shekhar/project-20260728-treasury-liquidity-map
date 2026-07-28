import unittest

from treasury_liquidity_map.models import Record
from treasury_liquidity_map.scoring import score_record


class DepthCheck47(unittest.TestCase):
    def test_047_control_mapping(self):
        record = Record(id="cashflow-047", exposure=47860, signal=0.456, urgency=8)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
