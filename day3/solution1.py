import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from day3.BatteryArrayParser import BatteryArrayParser
from utils.utils import Utils


def solve(input_text):
    verbose = os.environ.get('SOLUTION_VERBOSE', '0') == '1'

    batteryArrays = Utils.BatteryParser.parseBatteryArrays(input_text)
    batteryArrayParser = BatteryArrayParser(batteryArrays, verbose)

    return batteryArrayParser.calculate_total_output(2)



def main():
    Utils.Runner.run_solution(solve)


if __name__ == "__main__":
    main()
