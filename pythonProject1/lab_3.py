# Task1
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


# Task3

class SquareGenerator:
    def __init__(self):
        self.start = int(input("Enter start: "))
        self.ends = int(input("Enter end: "))

        squares = [x ** 2 for x in range(self.start, self.ends)]
        print("Squares:", squares)

start_class = SquareGenerator()

#Task 4