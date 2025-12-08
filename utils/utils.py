import sys
from pathlib import Path


class Grid:

    def __init__(self, grid_data):
        self.data = grid_data
        self.rows = len(grid_data)
        self.cols = len(grid_data[0]) if self.rows > 0 else 0

    def get(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        return None

    def is_valid_position(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols

    def count_adjacent(self, row, col, target_value, directions=None):
        if directions is None:
            directions = Utils.AdjacencyMatrixBuilder.DIRECTIONS_8

        count = 0
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if self.is_valid_position(nr, nc) and self.data[nr][nc] == target_value:
                count += 1
        return count

    def find_all(self, target_value):
        positions = []
        for r in range(self.rows):
            for c in range(self.cols):
                if self.data[r][c] == target_value:
                    positions.append((r, c))
        return positions

    def remove_positions(self, positions, replacement = '.'):
        for r, c in positions:
            if self.is_valid_position(r, c):
                self.data[r][c] = replacement

    def print(self):
        print("\n" + "=" * (self.cols + 2))
        for r in range(self.rows):
            row_str = ""
            for c in range(self.cols):
                row_str += self.data[r][c]
            print(row_str)
        print("=" * (self.cols + 2) + "\n")



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

    class GridParser:

        @staticmethod
        def parse_grid(input_text):
            lines = input_text.strip().split('\n')
            grid_data = [list(line) for line in lines]
            return Grid(grid_data)

    class AdjacencyMatrixBuilder:

        DIRECTIONS_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        DIRECTIONS_8 = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        @staticmethod
        def build_from_grid(grid, neighbor_count=8):
            rows = len(grid)
            cols = len(grid[0]) if rows > 0 else 0
            total_nodes = rows * cols

            adjacency_matrix = [[0] * total_nodes for _ in range(total_nodes)]

            if neighbor_count == 4:
                directions = Utils.AdjacencyMatrixBuilder.DIRECTIONS_4
            elif neighbor_count == 8:
                directions = Utils.AdjacencyMatrixBuilder.DIRECTIONS_8
            else:
                raise ValueError(f"neighbor_count must be 4 or 8, got {neighbor_count}")

            for r in range(rows):
                for c in range(cols):
                    current_node = Utils.AdjacencyMatrixBuilder.get_node_index(r, c, cols)

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if 0 <= nr < rows and 0 <= nc < cols:
                            neighbor_node = Utils.AdjacencyMatrixBuilder.get_node_index(nr, nc, cols)
                            adjacency_matrix[current_node][neighbor_node] = 1

            return adjacency_matrix

        @staticmethod
        def get_node_index(row, col, cols):
            return row * cols + col

        @staticmethod
        def get_coordinates(node_index, cols):
            return (node_index // cols, node_index % cols)

    class PaperParser:

        @staticmethod
        def parsePaper(input_text, neighbor_count=8):
            lines = input_text.strip().split('\n')

            grid = []
            for line in lines:
                grid.append(list(line))

            return Utils.AdjacencyMatrixBuilder.build_from_grid(grid, neighbor_count)

    @staticmethod
    def print_adjacency_matrix(matrix):
        for row in matrix:
            print(' '.join(str(cell) for cell in row))

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

    class IngredientParser:

        @staticmethod
        def parse_ingredient_database(input_text):
            sections = input_text.strip().split('\n\n')

            fresh_ranges = []
            range_lines = sections[0].strip().split('\n')
            for line in range_lines:
                start, end = line.split('-')
                fresh_ranges.append((int(start), int(end)))

            available_ingredients = []
            ingredient_lines = sections[1].strip().split('\n')
            for line in ingredient_lines:
                available_ingredients.append(int(line.strip()))

            return fresh_ranges, available_ingredients

        def parse_fresh_array(input_text):
            sections = input_text.strip().split('\n\n')

            fresh_ranges = []
            range_lines = sections[0].strip().split('\n')
            for line in range_lines:
                start, end = line.split('-')
                fresh_ranges.append((int(start), int(end)))

            return fresh_ranges

    class ProblemParser:

        def parse_problems(input_text):
            sections = input_text.strip().split("\n")
            new_sections = []

            for section in sections:
                new_sections.append(section.split(" "))
                i = 0
                n = len(new_sections[-1])
                while i < n:
                    if new_sections[-1][i].strip() == "":
                        new_sections[-1].pop(i)
                        n -= 1
                    else:
                        i += 1

            numbers = [[] for i in range(len(new_sections[0]))]
            for i in range(len(new_sections) - 1):
                section = new_sections[i]
                for j in range(len(section)):
                    numbers[j].append(int(section[j]))

            return numbers, new_sections[-1]

        def parse_cephalopod_problems(input_text):
            lines = input_text.strip().split("\n")

            max_length = max(len(line) for line in lines)

            padded_lines = [line.ljust(max_length) for line in lines]

            columns = []
            for i in range(max_length):
                column = ''.join(padded_lines[j][i] for j in range(len(padded_lines)))
                columns.append(column)

            problems = []
            current_problem = []

            for column in columns:
                if column.strip() == '':
                    if current_problem:
                        problems.append(current_problem)
                        current_problem = []
                else:
                    current_problem.append(column)

            if current_problem:
                problems.append(current_problem)

            numbers_lists = []
            operators_lists = []
            for problem in problems:
                numbers = []
                for col in problem:
                    if '*' in col:
                        operator = '*'
                        col.replace("*", '')
                    elif '+' in col:
                        operator = '+'
                        col.replace("+", '')
                    digits = ''.join(c for c in col if c.strip() and c.isdigit())
                    if digits:
                        numbers.append(int(digits))

                numbers.reverse()

                numbers_lists.append(numbers)
                operators_lists.append(operator)

            return numbers_lists, operators_lists

    class TachyonParser:
        def parse_manifold(input_text):
            return Utils.GridParser.parse_grid(input_text)

        def find_start(grid):
            positions = grid.find_all('S')
            return positions[0] if positions else None

    class JunctionParser:
        def parse_junctions(input_text):
            lines = input_text.splitlines()

            junction_boxes = []
            for line in lines:
                line = line.strip()
                if not line:
                    continue

                parts = [p.strip() for p in line.split(",")]
                junction_boxes.append(tuple(int(p) for p in parts))

            return junction_boxes

