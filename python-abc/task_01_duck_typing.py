#!/usr/bin/python3

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""
    
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Class representing a Circle."""
    
    def __init__(self, radius):
        """Initialize the Circle, allowing for negative radius.
        
        Args:
            radius (float): The radius of the Circle.
        """
        self.radius = radius  # Allow negative radius without raising an error.

    def area(self):
        """Calculate and return the area of the Circle."""
        # Return 0 for negative radius
        return math.pi * (self.radius ** 2) if self.radius >= 0 else 0

    def perimeter(self):
        """Calculate and return the perimeter of the Circle."""
        # Return 0 for negative radius
        return (2 * math.pi * self.radius) if self.radius >= 0 else 0


class Rectangle(Shape):
    """Class representing a Rectangle."""
    
    def __init__(self, width, height):
        """Initialize the Rectangle with non-negative width and height.
        
        Args:
            width (float): The width of the Rectangle.
            height (float): The height of the Rectangle.
        """
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative numbers.")
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the area of the Rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the Rectangle."""
      
