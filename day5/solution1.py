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

    fresh_ranges, available_ingredients = Utils.IngredientParser.parse_ingredient_database(input_text)

    if verbose:
        print(f"Fresh ranges: {fresh_ranges}")
        print(f"Available ingredients: {available_ingredients}")
        print()

    fresh_count = 0

    for ingredient_id in available_ingredients:
        if is_fresh(ingredient_id, fresh_ranges):
            fresh_count += 1
            if verbose:
                print(f"Ingredient ID {ingredient_id} is FRESH")
        else:
            if verbose:
                print(f"Ingredient ID {ingredient_id} is spoiled")

    return fresh_count


def main():
    Utils.Runner.run_solution(solve)


if __name__ == "__main__":
    main()
