#!/usr/bin/python3
"""
This is a module
"""

def read_file(filename=""):
    """
    this is a function that reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, 'r') as file:
        print(file.read(), end="")
