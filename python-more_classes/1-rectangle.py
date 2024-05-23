#!/usr/bin/python3

"""
Define a rectangle class
"""


class Rectangle:
    """
    Represent a rectangle.
    
    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """
    # Initialize the rectangle with optional width and height
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    # Retrieve the width of the rectangle
    @property
    def width(self):
        return self.__width

    # Set the width of the rectangle
    @width.setter
    def width(self, value):
        # Check if the width is an integer
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        # Check if the width is greater than or equal to 0
        if value < 0:
            raise ValueError("width must be >= 0")
        # Set the private width attribute
        self.__width = value

    # Retrieve the height of the rectangle
    @property
    def height(self):
        return self.__height

    # Set the height of the rectangle
    @height.setter
    def height(self, value):
        # Check if the height is an integer
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        # Check if the height is greater than or equal to 0
        if value < 0:
            raise ValueError("height must be >= 0")
        # Set the private height attribute
        self.__height = value