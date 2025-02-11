#!/usr/bin/python3
"""
This is a module
"""


def append_write(filename="", text=""):
    """
    a function that appends a string at the end of a text file
    """
    with open(filename, 'a') as f:
        return f.write(text)
