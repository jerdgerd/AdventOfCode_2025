import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from utils.utils import Utils
from day8.JunctionBoxConnector import JunctionBoxConnector

def solve(input_text):
    verbose = os.environ.get('SOLUTION_VERBOSE', '0') == '1'

    junction_boxes = Utils.JunctionParser.parse_junctions(input_text)
    junction_box_connector = JunctionBoxConnector(junction_boxes, verbose)

    junction_box_connector.connect_boxes(1000)
    return junction_box_connector.find_part_1_math()


def main():
    Utils.Runner.run_solution(solve)


if __name__ == "__main__":
    main()
