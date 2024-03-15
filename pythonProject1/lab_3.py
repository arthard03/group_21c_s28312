# Task1
import numpy as np

squares = [x ** 2 for x in range(1, 11)]

print(squares)


def generate_squares(start, end):
    squares = [x ** 2 for x in range(start, end + 1)]
    return squares


# Task2
start_num = 1
end_num = 10
squares_list = generate_squares(start_num, end_num)
print("List of squares from", (start_num, end_num))
print(squares_list)


# Task 3
# Task 4
# Task 5
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

