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
    
    @property
    def size(self):
        return self.__size

        
    @size.setter
    def size(self, value):
        if type(self.size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        area = self.__size * self.__size
        return area
