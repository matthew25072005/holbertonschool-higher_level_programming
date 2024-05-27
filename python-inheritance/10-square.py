#!/usr/bin/python3
"""A module that define a square"""
Rectangle = _import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Init values of Square(Rectangle)"""

        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)