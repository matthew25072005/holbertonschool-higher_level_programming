#!/usr/bin/python3
"""
This module defines a class BaseGeometry with a public instance method area.
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
