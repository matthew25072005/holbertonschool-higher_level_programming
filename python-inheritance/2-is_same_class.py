#!/usr/bin/python3
"""
This module defines a class named MyList.
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class, otherwise False.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
