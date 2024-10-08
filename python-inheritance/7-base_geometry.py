#!/usr/bin/python3
"""
This module defines a class BaseGeometry with methods for geometric operations.
"""


class BaseGeometry:
    """
    A class that represents base geometry concepts.
    """

    def area(self):
        """
        Raises an Exception indicating that the area method is not implemented.

        Raises:
            Exception: with the message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer, with the message <name> must be an integer.
            ValueError: If value is less than or equal to 0, with the message <name> must be greater than 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
