#!/usr/bin/python3
"""
This is a module
"""
import json


def load_from_json_file(filename):
    """
     function that creates an Object from a “JSON file”
    """
    with open(filename, 'w')as file:
        json.dump(data, file)
