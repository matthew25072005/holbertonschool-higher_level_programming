#!/usr/bin/python3
"""
This is a module
"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file
    """
    with open(filename, 'w') as f:
        return f.write(text)
