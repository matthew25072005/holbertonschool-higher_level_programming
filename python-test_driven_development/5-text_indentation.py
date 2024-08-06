#!/usr/bin/python3
"""Function to print a text with new lines after specific characters."""


def text_indentation(text):
    """Prints text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Replace the specified characters with themselves followed by new lines
    new_text = ""
    for char in text:
        if char in {'.', '?', ':'}:
            new_text += char + "\n\n"
        else:
            new_text += char
    
    # Remove extra new lines at the end of the text
    print("\n".join(line.strip() for line in new_text.splitlines() if line.strip()))
