#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or a subclass of a_class, otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
