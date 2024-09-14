#!/usr/bin/python3
"""
This module defines a function that adds two integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats, casting them to integers if necessary.
    
    Parameters:
    a (int, float): The first value.
    b (int, float, optional): The second value. Defaults to 98.
    
    Returns:
    int: The sum of the two values, cast to an integer.
    
    Raises:
    TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
