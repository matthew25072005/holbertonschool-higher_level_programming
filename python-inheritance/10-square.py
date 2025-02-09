#!/usr/bin/python3
"""
This is a module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class that inherites Rectangle
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size * self.__size

