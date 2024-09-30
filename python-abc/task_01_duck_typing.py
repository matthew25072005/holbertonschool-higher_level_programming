#!/usr/bin/python3
"""this module is about creating an abstract class named Shape using the ABC
package."""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract class representing a shape."""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Concrete class representing a circle."""

    def __init__(self, radius):
        self.radius = radius  # Permitir radio negativo

    def area(self):
        """Calcula el área del círculo."""
        return pi * self.radius**2 if self.radius >= 0 else 0

    def perimeter(self):
        """Calcula el perímetro del círculo."""
        return 2 * pi * self.radius if self.radius >= 0 else 0  # Devuelve 0 si el radio es negativo


class Rectangle(Shape):
    """Concrete class representing a rectangle."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calcula el área del rectángulo."""
        return self.width * self.height

    def perimeter(self):
        """Calcula el perímetro del rectángulo."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Imprime el área y perímetro de un objeto de forma."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

# Test cases
circle = Circle(5)
rectangle = Rectangle(4, 6)

shape_info(circle)
print("---")
shape_info(rectangle)

# Test negativo
circle_negative = Circle(-5)
shape_info(circle_negative)
