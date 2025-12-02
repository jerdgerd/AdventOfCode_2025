class Rotator:
    MIN_NUMBER = 0
    MAX_NUMBER = 99
    NUMBERS_IN_ROTATION = [i for i in range(MIN_NUMBER, MAX_NUMBER + 1)]
    CURRENT_POSITION = 50

    def __init__(self):
        self.current_position = self.CURRENT_POSITION
        self.hit_positions = {}
        self.hit_through_positions = {}

    def rotate(self, direction, num):
        old_position = self.current_position

        if direction == "left":
            self.current_position = (self.current_position - num) % (self.MAX_NUMBER + 1)
        elif direction == "right":
            self.current_position = (self.current_position + num) % (self.MAX_NUMBER + 1)

        self.hit_position_update(self.current_position)
        self.track_through_positions(old_position, self.current_position, direction, num)

    def rotate_multiple(self, rotations, verbose=False):
        if verbose:
            print(f"Starting position: {self.get_current_position()}")
            print(f"Processing {len(rotations)} rotations...")
            print("-" * 50)

        for direction, distance in rotations:
            self.rotate(direction, distance)
            if verbose:
                direction_symbol = "L" if direction == "left" else "R"
                print(f"Rotated {direction_symbol}{distance} → dial now at {self.get_current_position()}")

        if verbose:
            print("-" * 50)

    def track_through_positions(self, start, end, direction, distance):
        for i in range(1, distance + 1):
            if direction == "left":
                position = (start - i) % (self.MAX_NUMBER + 1)
            else:
                position = (start + i) % (self.MAX_NUMBER + 1)

            if position in self.hit_through_positions:
                self.hit_through_positions[position] += 1
            else:
                self.hit_through_positions[position] = 1

    def hit_position_update(self, num):
        if num in self.hit_positions:
            self.hit_positions[num] += 1
        else:
            self.hit_positions[num] = 1

    def get_current_position(self):
        return self.current_position

    def get_hit_positions(self):
        return self.hit_positions

    def get_hit_through_positions(self):
        return self.hit_through_positions

    def get_zero_count(self):
        return self.hit_positions.get(0, 0)

    def get_zero_through_count(self):
        return self.hit_through_positions.get(0, 0)
