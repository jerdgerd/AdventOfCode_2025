import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from day2.IdChecker import IdChecker
from utils.utils import Utils


def solve(input_text):
    verbose = os.environ.get('SOLUTION_VERBOSE', '0') == '1'

    ranges = Utils.IdCheckerParser.parseRanges(input_text)
    id_checker = IdChecker(ranges, verbose)
    id_checker.check_duplicate_ids()

    return id_checker.get_duplicate_sequence_twice_ids_sum()

def main():
    Utils.Runner.run_solution(solve)


if __name__ == "__main__":
    main()
