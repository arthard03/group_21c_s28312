import numpy as np


# Task 3
# Task 4
# Task 5
# Task 6
# Task 7
# Task 8
# Task 9
class SquareGenerator:
    def __init__(self):
        try:
            self.start = int(input("Enter start: "))
            self.end = int(input("Enter end: "))
            if self.end <= self.start:
                raise ValueError("End value must be smaller or equal.")
        except ValueError as e:
            print(e)
            self.start = 0
            self.end = 0

        squares = [x ** 2 for x in range(self.start, self.end)]
        print("Squares: ", squares)

        roots = [np.sqrt(x) for x in squares]
        print("Square roots: ", roots)


class CubicGenerator(SquareGenerator):
    def __init__(self):
        super().__init__()
    def generate_squares(self):
        if self.start > self.end:
            print("Error: Start value must smaller or equal.")
            return None
        # cubes = [x ** 3 for x in range(self.start, self.end)]
        squares = [x ** 2 for x in range(self.start, self.end)]
        print("Squares(from cubic class): ", squares)
        # print("Cubes: ", cubes)

        return squares

cube_generator = CubicGenerator()

result = cube_generator.generate_squares()

if result is None:
    print("Squares generation failed.")
