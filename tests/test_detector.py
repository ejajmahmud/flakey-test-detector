"""Unit tests for FlakeyTestDetector."""
import unittest
from flakey_test_detector.detector import FlakeyTestDetector

class TestFlakeyDetector(unittest.TestCase):
    def test_stable_pass(self):
        res = FlakeyTestDetector.evaluate(lambda: True, iterations=5)
        self.assertEqual(res["status"], "STABLE_PASS")
        self.assertFalse(res["is_flakey"])

    def test_stable_fail(self):
        res = FlakeyTestDetector.evaluate(lambda: False, iterations=5)
        self.assertEqual(res["status"], "STABLE_FAIL")
        self.assertFalse(res["is_flakey"])

    def test_flakey(self):
        state = [True, False, True]
        res = FlakeyTestDetector.evaluate(lambda: state.pop(0), iterations=3)
        self.assertTrue(res["is_flakey"])
        self.assertEqual(res["status"], "FLAKEY")

if __name__ == "__main__":
    unittest.main()
