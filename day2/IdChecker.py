import math

class IdChecker:

    def __init__(self, ids, verbose=False):
        self.id_ranges = ids
        self.duplicate_sequence_solely_ids = {}
        self.verbose = verbose
        self.seen = set()

    def generate_repeating_numbers(self, start, end):
        invalid_ids = {}

        start_len = len(str(start))
        end_len = len(str(end))

        for total_len in range(start_len, end_len + 1):
            for pattern_len in range(1, total_len // 2 + 1):
                if total_len % pattern_len == 0:
                    repetitions = total_len // pattern_len

                    pattern_start = 10 ** (pattern_len - 1) if pattern_len > 1 else 0
                    pattern_end = 10 ** pattern_len

                    for pattern in range(pattern_start, pattern_end):
                        num_str = str(pattern) * repetitions
                        num = int(num_str)

                        if start <= num <= end and num not in self.seen:
                            self.seen.add(num)
                            if repetitions not in invalid_ids:
                                invalid_ids[repetitions] = []
                            invalid_ids[repetitions].append(num)
                            if self.verbose:
                                print(f"  {num} is invalid (pattern '{pattern}' repeated {repetitions} times)")

        for rep in invalid_ids:
            invalid_ids[rep] = sorted(set(invalid_ids[rep]))

        return invalid_ids

    def check_duplicate_ids(self):
        self.duplicate_sequence_solely_ids = {}

        for start, end in self.id_ranges:
            if self.verbose:
                print(f"\nChecking range {start}-{end}:")

            invalid_in_range = self.generate_repeating_numbers(start, end)

            for repetitions, ids in invalid_in_range.items():
                if repetitions not in self.duplicate_sequence_solely_ids:
                    self.duplicate_sequence_solely_ids[repetitions] = []
                self.duplicate_sequence_solely_ids[repetitions].extend(ids)

        for rep in self.duplicate_sequence_solely_ids:
            self.duplicate_sequence_solely_ids[rep] = sorted(set(self.duplicate_sequence_solely_ids[rep]))

        if self.verbose:
            total_count = sum(len(ids) for ids in self.duplicate_sequence_solely_ids.values())
            print(f"\nTotal invalid IDs found: {total_count}")
            print(f"Grouped by repetitions: {dict((k, len(v)) for k, v in self.duplicate_sequence_solely_ids.items())}")

        return self.duplicate_sequence_solely_ids

    def get_duplicate_sequence_twice_ids_sum(self):
        return sum(self.duplicate_sequence_solely_ids[2])

    def get_duplicate_sequence_solely_ids_sum(self):
        return sum(id_num for ids in self.duplicate_sequence_solely_ids.values() for id_num in ids)
