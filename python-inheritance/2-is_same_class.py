#!/usr/bin/python3
"""
This is a module
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class, otherwise False.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
