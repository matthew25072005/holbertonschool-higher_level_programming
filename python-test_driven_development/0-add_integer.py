#!/usr/bin/python3
"""This module defines a function to add two integers."""

def add_integer(a, b=98):
    """Add two integers.

    Args:
        a (int, float): The first number.
        b (int, float, optional): The second number. Defaults to 98.

    Returns:
        int: The sum of the two numbers, casted to an integer.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
