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

    ways = {}
    ways[start_pos] = 1

    while queue:
        pos = queue.pop(0)
        beams = ways[pos]

        if not grid.is_valid_position(pos[0], pos[1]):
            continue

        down_pos = (pos[0] + 1, pos[1])
        if not grid.is_valid_position(down_pos[0], down_pos[1]):
            continue

        if grid.get(down_pos[0], down_pos[1]) == '^':
            left_pos = (pos[0] + 1, pos[1] - 1)
            right_pos = (pos[0] + 1, pos[1] + 1)

            grid.remove_positions([left_pos, right_pos], '|')

            if grid.is_valid_position(left_pos[0], left_pos[1]):
                if left_pos not in ways:
                    ways[left_pos] = 0
                ways[left_pos] += beams
                if left_pos not in queue:
                    queue.append(left_pos)

            if grid.is_valid_position(right_pos[0], right_pos[1]):
                if right_pos not in ways:
                    ways[right_pos] = 0
                ways[right_pos] += beams
                if right_pos not in queue:
                    queue.append(right_pos)

            if verbose:
                print(f"\nHit splitter at ({pos[0] + 1}, {pos[1]}). Beam count {beams}")
                grid.print()
        else:
            next_pos = (pos[0] + 1, pos[1])

            grid.remove_positions([[next_pos[0], next_pos[1]]], '|')

            if grid.is_valid_position(next_pos[0], next_pos[1]):
                if next_pos not in ways:
                    ways[next_pos] = 0
                ways[next_pos] += beams
                if next_pos not in queue:
                    queue.append(next_pos)

    res = 0
    for i in range(grid.cols):
        if (grid.rows - 1, i) in ways:
            res += ways[(grid.rows - 1, i)]
            if verbose:
                print(grid.rows - 1, i, ways[(grid.rows - 1, i)])

    return res


def main():
    Utils.Runner.run_solution(solve)


if __name__ == "__main__":
    main()
