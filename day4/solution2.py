import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from utils.utils import Utils


def solve(input_text):
    verbose = os.environ.get('SOLUTION_VERBOSE', '0') == '1'

    grid = Utils.GridParser.parse_grid(input_text)

    total_removed = 0

    while True:
        paper_rolls = grid.find_all('@')

        if not paper_rolls:
            break

        accessible_rolls = []

        for r, c in paper_rolls:
            adjacent_count = grid.count_adjacent(r, c, '@')

            if adjacent_count < 4:
                accessible_rolls.append((r, c))

        if not accessible_rolls:
            break

        grid.remove_positions(accessible_rolls)

        removed_count = len(accessible_rolls)
        total_removed += removed_count

        if verbose:
            print(f"Removed {removed_count} rolls (total: {total_removed})")
            print(f"Accessible positions: {accessible_rolls}")
            print()

    return total_removed


def main():
    Utils.Runner.run_solution(solve)


if __name__ == "__main__":
    main()
