#!/usr/bin/python3
"""
Module 8-rectangle

This module contains the definition of a Rectangle class that inherits from
BaseGeometry. The Rectangle class is used to represent rectangles with width
and height, both of which are validated to be positive integers.
"""


from base_geometry_7_2 import BaseGeometry

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
