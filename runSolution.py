#!/usr/bin/env python3

import sys
import os
import subprocess
from pathlib import Path


class SolutionRunner:

    def __init__(self, base_dir="."):
        self.base_dir = Path(base_dir)

    def find_solution_file(self, day, solution):
        solution_path = self.base_dir / f"day{day}" / f"solution{solution}.py"

        if not solution_path.exists():
            raise FileNotFoundError(f"Solution file not found: {solution_path}")

        return solution_path

    def find_input_file(self, day, solution):
        input_path = self.base_dir / f"day{day}" / f"solution{solution}.txt"

        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")

        return input_path

    def run_solution(self, day, solution, verbose=False):

        try:
            solution_file = self.find_solution_file(day, solution)
            input_file = self.find_input_file(day, solution)

            print(f"Running: {solution_file}")
            print(f"Input: {input_file}")
            if verbose:
                print(f"Verbose mode: ON")
            print("-" * 50)

            env = os.environ.copy()
            env['SOLUTION_VERBOSE'] = '1' if verbose else '0'

            result = subprocess.run(
                [sys.executable, str(solution_file), str(input_file)],
                env=env,
                check=False
            )

            return result.returncode

        except FileNotFoundError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1
        except Exception as e:
            print(f"Unexpected error: {e}", file=sys.stderr)
            return 1


def main():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Usage: python runSolution.py <day> <solution> [--verbose|-v]")
        print("Example: python runSolution.py 1 1")
        print("Example: python runSolution.py 1 1 --verbose")
        sys.exit(1)

    try:
        day = int(sys.argv[1])
        solution = int(sys.argv[2])
    except ValueError:
        print("Error: Day and solution must be integers")
        sys.exit(1)

    # Check for verbose flag
    verbose = False
    if len(sys.argv) == 4:
        if sys.argv[3] in ['--verbose', '-v']:
            verbose = True
        else:
            print(f"Error: Unknown flag '{sys.argv[3]}'")
            print("Use --verbose or -v for verbose output")
            sys.exit(1)

    runner = SolutionRunner()
    exit_code = runner.run_solution(day, solution, verbose)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
