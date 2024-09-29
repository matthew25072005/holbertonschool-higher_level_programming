#!/usr/bin/python3
"""
Module 11-square
This module defines a Square class that inherits from Rectangle.
The Square class represents a square defined by its size,
validating the size as a positive integer and implementing
the area method.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    Represents a square defined by its size.
    """

    def __init__(self, size):
        """
        Initialize the square with size.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: Description of the square in the format
                 [Square] <size>/<size>.
        """
        return f"[Square] {self.__size}/{self.__size}"
