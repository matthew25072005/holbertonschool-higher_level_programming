#!/usr/bin/python3
"""
This is a module
"""
from abc import ABC, abstractmethod
import math  # Importar el módulo math

class Shape(ABC):
    """
    An abstract class named Shape
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

def shape_info(shape):
    """
    Function to print the area and perimeter of a shape.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

class Circle(Shape):
    """
    Concrete class for Circle
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        if self.radius < 0:
            return 0
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        if self.radius < 0:
            return 0
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """
    Concrete class for Rectangle
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

