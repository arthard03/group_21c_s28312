from pythonProject1.square_generator import SquareGenerator


class CubicGenerator(SquareGenerator):
    def __init__(self):
        super().__init__()
    def generate_cubes(self):
        self.cubes = [x ** 3 for x in range(self.start, self.end)]
        return self.cubes

    def print_cubes(self):
        print("Cubes: ", self.cubes)
