#!/usr/bin/python3
"""Python executable file."""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

"""Load the existing list if the file exists."""
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

"""Add the command-line arguments to the list."""
items.extend(sys.argv[1:])

"""Save the updated list back to the file."""
save_to_json_file(items, filename)
