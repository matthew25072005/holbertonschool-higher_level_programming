#!/usr/bin/python3
"""
This module defines a class named Rectangle.
"""


class Rectangle:
    """
    Represents a rectangle.
    """

    def width(self, value):
        self.__width = width
        if width is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        
    def height(self, value):
        self.__height = height
        if height is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
    
    def __init__(self, width=0, height=0):
        pass
