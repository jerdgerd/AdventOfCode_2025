import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from utils.utils import Utils


def solve(input_text):
    verbose = os.environ.get('SOLUTION_VERBOSE', '0') == '1'

    grid = Utils.TachyonParser.parse_manifold(input_text)
    start_pos = Utils.TachyonParser.find_start(grid)

    queue = [start_pos]
    res = 0

    while queue:
        pos = queue.pop(0)

        if not grid.is_valid_position(pos[0], pos[1]):
            continue

        if grid.get(pos[0] + 1, pos[1]) == '^':
            left_pos = (pos[0] + 1, pos[1] - 1)
            right_pos = (pos[0] + 1, pos[1] + 1)

            grid.remove_positions([left_pos, right_pos], '|')

            if left_pos not in queue:
                queue.append(left_pos)
            if right_pos not in queue:
                queue.append(right_pos)

            res += 1

            if verbose:
                print(f"\nHit splitter at ({pos[0] + 1}, {pos[1]}). Split count: {res}")
                grid.print()
        else:
            next_pos = (pos[0] + 1, pos[1])
            if next_pos not in queue:
                grid.remove_positions([[next_pos[0], next_pos[1]]], '|')
                queue.append(next_pos)

    return res


def main():
    Utils.Runner.run_solution(solve)


if __name__ == "__main__":
    main()
