#!/usr/bin/env python3
"""
Module task_01_duck_typing
This module defines an abstract base class Shape and two concrete
classes Circle and Rectangle that implement area and perimeter methods.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class representing a Shape."""

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Class representing a Circle, inheriting from Shape."""

    def __init__(self, radius):
        """Initialize the Circle with a radius.
        
        Args:
            radius (float): The radius of the Circle.
        """
        self.__radius = radius

    def area(self):
        """Calculate and return the area of the Circle."""
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """Calculate and return the perimeter of the Circle."""
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """Class representing a Rectangle, inheriting from Shape."""

    def __init__(self, width, height):
        """Initialize the Rectangle with width and height.
        
        Args:
            width (float): The width of the Rectangle.
            height (float): The height of the Rectangle.
        """
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the Rectangle."""
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """Print the area and perimeter of the given shape.

    Args:
        shape (Shape): An instance of a class that inherits from Shape.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
