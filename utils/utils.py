import sys
from pathlib import Path


class Utils:

    class ArrayParser:

        def parse_lines(text):
            return text.strip().split('\n')

        def parse_to_array(text, delimiter=' ', trim=True):
            lines = Utils.ArrayParser.parse_lines(text)
            result = []

            for line in lines:
                elements = line.split(delimiter)
                if trim:
                    elements = [element.strip() for element in elements]
                result.append(elements)

            return result

    class RotationParser:

        @staticmethod
        def parse_rotations(input_text):
            rotations = []
            parsed_array = Utils.ArrayParser.parse_to_array(input_text, delimiter=' ', trim=True)
            tokens = [token for line in parsed_array for token in line if token]

            for token in tokens:
                direction_char = token[0]
                distance = int(token[1:])
                direction = "left" if direction_char == "L" else "right"
                rotations.append((direction, distance))

            return rotations

    class IdCheckerParser:

        @staticmethod
        def parseRanges(input_text):
            parsed_ranges = Utils.ArrayParser.parse_to_array(input_text, delimiter=',', trim=True)[0]
            return [tuple(int(x) for x in parsed_ranges[i].split('-')) for i in range(len(parsed_ranges))]

    class BatteryParser:

        @staticmethod
        def parseBatteryArrays(input_text):
            lines = Utils.ArrayParser.parse_lines(input_text)
            arrays = [[int(digit) for digit in line] for line in lines]
            return arrays

    class Runner:

        @staticmethod
        def run_solution(solve_function):
            if len(sys.argv) != 2:
                print("Usage: python solution.py <input_file>", file=sys.stderr)
                sys.exit(1)

            input_file = Path(sys.argv[1])

            if not input_file.exists():
                print(f"Error: Input file '{input_file}' not found", file=sys.stderr)
                sys.exit(1)

            try:
                input_text = input_file.read_text()
                result = solve_function(input_text)
                print(f"\n{'=' * 50}")
                print(f"FINAL ANSWER: {result}")
                print(f"{'=' * 50}")

            except Exception as e:
                print(f"Error processing solution: {e}", file=sys.stderr)
                import traceback
                traceback.print_exc()
                sys.exit(1)
