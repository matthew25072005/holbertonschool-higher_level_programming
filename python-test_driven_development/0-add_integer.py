#!/usr/bin/python3
"""Add integer function."""

def add_integer(a, b=98):
    """ 
    Returns the sum of 'a' and 'b'.
    
    Args:
        a (int): first integer to be added to sum.
        b (int): second integer to be added to sum.
    
    Returns:
        int: The sum of a + b
    Raises:
        TypeError: "{a or b} must be an integer"
    """
    
    # Check for NaN by using the fact that NaN is not equal to itself
    if a != a:
        raise TypeError("a must be an integer")
    if b != b:
        raise TypeError("b must be an integer")
    
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
