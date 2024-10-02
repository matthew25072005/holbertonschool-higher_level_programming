#!/usr/bin/python3
"""
This module provides a function to read a UTF-8 encoded text file and print its content to stdout.

The module contains the following function:
    - read_file: Reads and prints the content of a specified file.
"""

def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints its content to stdout.

    Args:
        filename (str): The name of the file to be read. 
                        Defaults to an empty string, which expects the filename to be provided during the function call.

    This function opens the file specified by the 'filename' argument in read mode using UTF-8 encoding.
    It then reads the entire content of the file and prints it to the standard output (stdout). 
    The 'with' statement is used to ensure that the file is properly closed after being read.
    
    Example usage:
        read_file("example.txt")  # Reads and prints the content of example.txt
    """
    # Open the file with UTF-8 encoding and read its content
    with open(filename, "r", encoding="UTF-8") as file:  # Corrected "whit" and "UFT-8" to "with" and "UTF-8"
        # Print the content of the file, ensuring no extra newline is added after the content
        print(file.read(), end="")
