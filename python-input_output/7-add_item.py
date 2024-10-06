#!/usr/bin/python3
"""
Script that adds all arguments to a Python list,
and then saves them to a file.
"""
import sys
import os

# Import functions from previous files
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# File where the list will be stored
filename = "add_item.json"

# Check if the file exists, and load its content
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add new arguments from command line (ignoring the script name)
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)
