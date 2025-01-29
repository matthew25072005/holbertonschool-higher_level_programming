#!/usr/bin/python3
"""
This module defines a class named Square.
"""


class Square:
    """
    Represents a square.
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        area = size * size
        return area
