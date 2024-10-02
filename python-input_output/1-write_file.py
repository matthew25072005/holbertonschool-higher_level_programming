#!/usr/bin/python3
"""
This module provides a function to write a string to a text file
(UTF-8 encoded) and returns the number of characters written.

The function is designed to:
- Create a new file if it doesn't exist.
- Overwrite the content of the file if it already exists.
- Handle the file operations using the `with` statement to ensure
proper resource management.

Functions:
    write_file(filename="", text=""): Writes a string to a file
    and returns the number of characters written.
"""

def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns the number of
    characters written.

    Args:
        filename (str): The name of the file to write to. If no
                        filename is provided, an empty string is
                        used, which would typically result in an
                        error.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written to the file.

    The function opens the file in write mode ('w'), which means it
    will overwrite the file if it already exists, and create it if
    it does not exist. It uses UTF-8 encoding to ensure proper
    handling of characters in the text.
    """

    # Open the file in write mode with UTF-8 encoding
    with open(filename, "w", encoding="UTF-8") as file:
        # Write the provided text to the file and store the number
        # of characters written
        n_o_c = file.write(text)

    # Return the number of characters written to the file
    return n_o_c
