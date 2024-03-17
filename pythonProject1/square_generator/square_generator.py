import numpy as np


# Task 3
# Task 4
# Task 5
# Task 6
class SquareGenerator:
    def __init__(self):
        try:
            self.start = int(input("Enter start: "))
            self.end = int(input("Enter end: "))
            if self.end <= self.start:
                raise ValueError("End value must be smaller than start or equal .")
        except ValueError as e:
            print(e)
            self.start = 0
            self.end = 0

        # Generate a list of squares
        squares = [x ** 2 for x in range(self.start, self.end)]
        print("Squares: ", squares)

        # Calculate square roots
        roots = [np.sqrt(x) for x in squares]
        print("Square roots: ", roots)

start_class = SquareGenerator()