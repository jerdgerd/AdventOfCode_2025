import math

class ProblemSolver:

    def __init__(self, symbol, numbers, verbose=False):
        self.symbol = symbol
        self.numbers = numbers
        self.verbose = verbose

    def return_closure(self):
        if self.symbol == '+':
            return lambda nums: sum(nums)
        elif self.symbol == "*":
            return lambda nums: math.prod(nums)
        else:
            raise ValueError(f"Unsupported symbol: {self.symbol}")

    def solve_problem(self):
        closure_func = self.return_closure()
        return closure_func(self.numbers)
