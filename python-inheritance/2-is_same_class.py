#!/usr/bin/python3:
'''
Write a function that returns True if the object is exactly
an instance of the specified class; otherwise False.
'''


def is_same_class(obj, a_class):
    """return if its the same class"""

    return issubclass(a_class, type(obj))
