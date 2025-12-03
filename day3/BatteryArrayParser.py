import math
from itertools import combinations

class BatteryArrayParser:

    def __init__(self, batteryArrays, verbose=False):
        self.batteryArrays = batteryArrays
        self.verbose = verbose

    def find_max_joltage_for_bank(self, bank, num_batteries=2):
        if len(bank) < num_batteries:
            return 0

        selected_positions = []

        for position_needed in range(num_batteries):
            best_digit = -1
            best_pos = -1
            start_search = selected_positions[-1] + 1 if selected_positions else 0

            remaining_batteries = num_batteries - position_needed - 1
            end_search = len(bank) - remaining_batteries

            for i in range(start_search, end_search):
                if int(bank[i]) > best_digit:
                    best_digit = int(bank[i])
                    best_pos = i

            selected_positions.append(best_pos)

        joltage_str = ''.join(str(bank[pos]) for pos in selected_positions)
        return int(joltage_str)

    def calculate_total_output(self, num_batteries=2):
        total = 0

        for bank in self.batteryArrays:
            max_joltage = self.find_max_joltage_for_bank(bank, num_batteries)
            total += max_joltage

            if self.verbose:
                print(f"Bank '{bank}' max joltage: {max_joltage}")

        if self.verbose:
            print(f"\nTotal output joltage: {total}")

        return total
