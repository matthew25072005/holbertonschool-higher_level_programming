#!/usr/bin/python3
"""This is the square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """define square from Rectangle"""

    def __init__(self, size):
        """init values of square"""

        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Define str for square"""

        return ("[Square {}/{}".format(self.__size, self.__size))