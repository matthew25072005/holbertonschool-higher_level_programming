#!/usr/bin/python3
"""
This is a module
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    an abstract class named Shape
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def shape_info(shape):
        pass

class Circle(Shape):
    """
    concrete class
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14159 * self.radius

    def shape_info(shape):
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")

class Rectangle(Shape):
    """
    concrete class
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 + self.height * 2

    def shape_info(shape):
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")
