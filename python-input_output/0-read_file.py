#!/usr/bin/python3
"""read_file.py: A function to read a text file (UTF8) and print it to stdout."""

def read_file(filename=""):
    """Read a text file (UTF8) and print it to stdout.

    Uses the 'with' statement to open the file and ensures it is closed after
    reading. Does not handle file permission or file does not exist exceptions.

    :param filename: The name of the file to read. Defaults to an empty string,
                     which will result in reading from standard input.
    """
    if filename:
        # Open the file in read mode with UTF8 encoding
        with open(filename, 'r', encoding='utf8') as file:
            # Read the file content and print it to stdout
            print(file.read())
    else:
        # If no filename is provided, read from standard input
        print(input("Enter text to print: "))
