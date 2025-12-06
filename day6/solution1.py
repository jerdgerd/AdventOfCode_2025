import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from utils.utils import Utils
from day6.ProblemSolver import ProblemSolver

def solve(input_text):
    verbose = os.environ.get('SOLUTION_VERBOSE', '0') == '1'

    numbers, symbols = Utils.ProblemParser.parse_problems(input_text)

    if verbose:
        for i in range(len(numbers)):
            print(f"Problem Numbers: {numbers[i]}")
            print(f"Problem Symbol: {symbols[i]}")
            print()

    res = 0
    for i in range(len(numbers)):
        problemSolver = ProblemSolver(symbols[i], numbers[i], verbose)
        res += problemSolver.solve_problem()

    return res


def main():
    Utils.Runner.run_solution(solve)


if __name__ == "__main__":
    main()
