from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, side, other):
        self.side = side
        self.other = other

    def calculate_area(self):
        return (self.side * self.other) / 2


class AreaCalculator:
    def __init__(self, shapes):

        assert isinstance(shapes, list), "'shape' should be of type 'list'."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calculate_area()

        return total


shapes = [Rectangle(2, 3), Triangle(2, 3)]
calculator = AreaCalculator(shapes)
print("The total area is:", calculator.total_area)