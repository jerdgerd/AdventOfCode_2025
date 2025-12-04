import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from utils.utils import Utils


def solve(input_text):
    verbose = os.environ.get('SOLUTION_VERBOSE', '0') == '1'

    grid = Utils.GridParser.parse_grid(input_text)

    paper_rolls = grid.find_all('@')

    accessible_count = 0

    for r, c in paper_rolls:
        adjacent_count = grid.count_adjacent(r, c, '@')

        if adjacent_count < 4:
            accessible_count += 1
            if verbose:
                print(f"Accessible roll at ({r}, {c}) with {adjacent_count} neighbors")

    return accessible_count


def main():
    Utils.Runner.run_solution(solve)


if __name__ == "__main__":
    main()
