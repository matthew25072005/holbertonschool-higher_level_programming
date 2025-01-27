#!/usr/bin/python3
"""
Function that adds two integers (or floats) and returns an integer.
"""

def add_integer(a, b=98):
    """Adds two integers or floats."""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
