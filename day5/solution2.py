import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from utils.utils import Utils

def is_fresh(ingredient_id, fresh_ranges):
    for start, end in fresh_ranges:
        if start <= ingredient_id <= end:
            return True
    return False

def solve(input_text):
    verbose = os.environ.get('SOLUTION_VERBOSE', '0') == '1'

    fresh_ranges = Utils.IngredientParser.parse_fresh_array(input_text)

    sorted_ranges = sorted(fresh_ranges, key=lambda x: x[0])

    if verbose:
        print(f"Original ranges: {fresh_ranges}")
        print(f"Sorted ranges: {sorted_ranges}")
        print()

    merged_ranges = [sorted_ranges[0]]

    for current_start, current_end in sorted_ranges[1:]:
        last_start, last_end = merged_ranges[-1]

        if current_start <= last_end + 1:
            merged_ranges[-1] = (last_start, max(last_end, current_end))
        else:
            merged_ranges.append((current_start, current_end))

    if verbose:
        print(f"Merged ranges: {merged_ranges}")
        print()

    fresh_count = 0
    for start, end in merged_ranges:
        count = (end - start) + 1
        fresh_count += count
        if verbose:
            print(f"Range ({start}, {end}): {count} IDs")

    return fresh_count


def main():
    Utils.Runner.run_solution(solve)


if __name__ == "__main__":
    main()
