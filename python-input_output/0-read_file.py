#!/usr/bin/python3

def read_file(filename=""):
    """Read a text file (UTF8) and print it to stdout.

    Uses the 'with' statement to open the file and ensures it is closed after
    reading. Does not handle file permission or file does not exist exceptions.

    :param filename: The name of the file to read. Defaults to an empty string,
                     which will result in reading from standard input.
    """
    if filename:
        with open(filename, 'r', encoding='utf8') as file:
            print(file.read())
    else:
        print(input("Enter text to print: "))
        