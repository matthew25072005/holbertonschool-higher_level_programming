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
        """Initialize the Circle with a non-negative radius.
        
        Args:
            radius (float): The radius of the Circle.
        """
        if radius < 0:
            raise ValueError("Radius must be a non-negative number.")
        self.radius = radius

    def area(self):
        """Calculate and return the area of the Circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate and return the perimeter of the Circle."""
        return 2 * math.pi * self.radius


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
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of the given shape.
    
    Args:
        shape (Shape): An instance of a class that inherits from Shape.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))

if __name__ == "__main__":
    try:
        circle = Circle(0)
        rectangle = Rectangle(5, 10)

        print("Circle:")
        shape_info(circle)
        
        print("\nRectangle:")
        shape_info(rectangle)
    except ValueError as e:
        print(e)
