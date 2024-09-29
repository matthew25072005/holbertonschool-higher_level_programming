#!/usr/bin/python3
"""
Module 8-rectangle
This module contains the definition of a Rectangle class that inherits from
BaseGeometry. The Rectangle class is used to represent rectangles with width
and height, both of which are validated to be positive integers.
"""

class BaseGeometry:
    """Base class for geometry."""
    
    def area(self):
        """Raises an Exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validates that value is a positive integer.
        
        Args:
            name (str): The name of the parameter.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """Class that represents a rectangle."""
    
    def __init__(self, width, height):
        """Initialize the rectangle with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
