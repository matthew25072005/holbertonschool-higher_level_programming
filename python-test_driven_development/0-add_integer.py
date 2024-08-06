#!/usr/bin/python3
"""A module to add two integers."""


def add_integer(a, b=98):
    """Add two integers.

    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add (defaults to 98).

    Returns:
        int: The sum of the two numbers.

    Raises:
        TypeError: If either `a` or `b` are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
