#!/usr/bin/python3
"""
This module contains a function that prints a text with two new lines after
each of these characters: '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Prints a text with two new lines after each of the characters: '.', '?', and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    # Loop through each character in the text
    i = 0
    while i < len(text):
        if text[i] in ['.', '?', ':']:
            # Print the character and add two new lines
            print(text[i], end="\n\n")
            # Skip any spaces following the punctuation
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            # Print the current character
            print(text[i], end="")
            i += 1
