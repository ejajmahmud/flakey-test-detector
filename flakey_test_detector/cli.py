"""Command-line interface for Flakey Test Detector."""
import random
import argparse
from .detector import FlakeyTestDetector

def main():
    parser = argparse.ArgumentParser(description="Flakey Test Detector CLI")
    parser.add_argument("--demo", action="store_true", help="Demonstrate flakiness detection")
    args = parser.parse_args()

    # Simulate non-deterministic test
    def intermittent_network_test():
        return random.random() > 0.3  # 70% pass rate

    report = FlakeyTestDetector.evaluate(intermittent_network_test, iterations=20)
    print("Flakiness Evaluation Result:")
    print(f"  Status: {report['status']}")
    print(f"  Pass Rate: {report['pass_rate'] * 100}% ({report['passes']}/{report['iterations']})")
    print(f"  Is Flakey? {report['is_flakey']}")

if __name__ == "__main__":
    main()
