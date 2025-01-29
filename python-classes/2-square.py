#!/usr/bin/python3
"""
This module defines a class named Square.
"""


class Square:
    """
    Represents a square.
    """
    def __init__(self, size):
        self.__size = size
        if size.isdigit():
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
