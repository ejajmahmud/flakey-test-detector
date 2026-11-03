"""Statistical repeat test runner for detecting non-deterministic flakiness."""
from typing import Callable, Dict, Any


class FlakeyTestDetector:
    @staticmethod
    def evaluate(test_fn: Callable[[], bool], iterations: int = 10) -> Dict[str, Any]:
        passes = 0
        failures = 0

        for _ in range(iterations):
            try:
                res = test_fn()
                if res:
                    passes += 1
                else:
                    failures += 1
            except Exception:
                failures += 1

        pass_rate = passes / iterations
        is_flakey = (0 < passes < iterations)

        status = "STABLE_PASS" if passes == iterations else ("STABLE_FAIL" if failures == iterations else "FLAKEY")

        return {
            "iterations": iterations,
            "passes": passes,
            "failures": failures,
            "pass_rate": round(pass_rate, 4),
            "is_flakey": is_flakey,
            "status": status
        }
