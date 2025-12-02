import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from day1.Rotator import Rotator
from utils.utils import Utils


def solve(input_text):
    verbose = os.environ.get('SOLUTION_VERBOSE', '0') == '1'

    rotations = Utils.RotationParser.parse_rotations(input_text)
    rotator = Rotator()

    rotator.rotate_multiple(rotations, verbose=verbose)

    zero_count = rotator.get_zero_through_count()
    print(f"\nDial passed through 0 a total of {zero_count} times")
    print(f"Password: {zero_count}")

    return zero_count


def main():
    Utils.Runner.run_solution(solve)


if __name__ == "__main__":
    main()
