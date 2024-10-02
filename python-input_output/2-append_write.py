#!/usr/bin/python3
"""
Module to append a string to the end of a text file (UTF-8) and return
the number of characters added.

This module provides a single function:
    - append_write(filename="", text=""): Appends text to a file and
    returns the number of characters added.
"""

def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF-8) and returns
    the number of characters added.

    Args:
        filename (str): The name of the file to append the string to.
                        If the file does not exist, it will be created.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="UTF-8") as file:
        cont_of_filename = file.write(text)
        return cont_of_filename
