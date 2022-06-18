class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
        self.mass_1m = 25
        self.depth = 5
        self.final_mass = self._length * self._width * self.mass_1m * self.depth

    def mass_method(self):
        mass = f'{self._length}м * {self._width}м * {self.mass_1m}кг * {self.depth}см = {self.final_mass} т'
        return mass

r1 = Road(23, 1231)
print(r1.mass_method())
r1 = Road(221, 421)
print(r1.mass_method())
r1 = Road(521, 421)
print(r1.mass_method())