#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance of,
or if it is an instance of a class that inherited from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Determines if the object is an instance of, or if it is an instance of a class
    that inherited from, the specified class.

    Args:
        obj (Any): The object to be checked.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance or inherited from a_class, False otherwise.
    """
    return isinstance(obj, a_class)
