#!/usr/bin/python3
""" 
Module to load a Python object from a JSON file.
"""

import json

def load_from_json_file(filename):
    """
    Creates an object from a JSON file.
    
    Args:
        filename (str): The name of the JSON file to read from.
        
    Returns:
        object: The Python object created from the JSON representation.
    """
    # Open the specified JSON file in read mode
    with open(filename, 'r') as f:
        # Load the content of the JSON file and return it as a Python object
        return json.load(f)
