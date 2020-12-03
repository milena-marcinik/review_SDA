"""
The example of abstract class with abc module.
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """The abstract class"""

    @abstractmethod
    def perimeter(self) -> float:
        """Returns the perimeter of shape"""
        pass

    @abstractmethod
    def area(self) -> float:
        """Returns the are of shape"""
        pass


class Rectangle(Shape):
    """A derived subclass, must implement the abstract methods."""
    def __init__(self, side_a: float, side_b: float):
        self.side_a = side_a
        self.side_b = side_b

    def perimeter(self) -> float:
        """Overriding abstract method"""
        return 2 * self.side_a + 2 * self.side_b

    def area(self) -> float:
        """Overriding abstract method"""
        return self.side_a * self.side_b


class Circle(Shape):
    """A derived subclass, must implement the abstract methods."""
    def __init__(self, radius: float):
        self.radius = radius

    def perimeter(self) -> float:
        """Overriding abstract method"""
        return 2 * pi * self.radius

    def area(self) -> float:
        """Overriding abstract method"""
        return pi * self.radius ** 2


rect = Rectangle(2, 3)
cir = Circle(4)
print(rect.perimeter())
print(cir.area())
