from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area():
        pass

    @abstractmethod
    def get_parameters(self):
        pass

    def __str__(self):
        return self.__class__.__name__
    
    def __eq__(self, value):
        return self.area() == value.area()
    def __lt__(self, other):
        return self.area() < other.area()
    def __gt__(self, other):
        return self.area() > other.area()
    def __le__(self, other):
        return self.area() <= other.area()
    def __ge__(self, other):
        return self.area() >= other.area()
    

class Circle(Shape):
    def __init__(self, radius):
        try:
            self._radius = float(radius)
        except ValueError:
            raise ValueError("Радиус должен быть числом")

    def area(self):
        return math.pi * self._radius ** 2

    def get_parameters(self):
            return f"Радиус: {self._radius}"

class Rectangle(Shape):
    def __init__(self, a, b):
        try:
            self._a = float(a)
            self._b = float(b)
        except ValueError:
            raise ValueError("Длина и ширина должны быть числами")

    def area(self):
        return self._a * self._b

    def get_parameters(self):
        return f"Ширина прямоугольника: {self._a}, высота: {self._b}"

# cir = Circle(5)
# cir2 = Circle(10)
# rect = Rectangle(5,62)
# rect2 = Rectangle(31, 10)

# print(cir2.area(), rect.area(), rect == rect2)
# print(rect)
# print(rect.get_parameters())
# print(cir2.get_parameters())