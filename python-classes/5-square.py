#!/usr/bin/python3
"""
This module defines a class named Square.
"""


class Square:
    """
    Represents a square.
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        area = self.size * self.size
        return area

    def my_print(self):
        i = 0
        o = 0
        if self.size == 0:
            print("")
        else:
            while i < self.size:
                print('#' * self.size)
                i += 1
