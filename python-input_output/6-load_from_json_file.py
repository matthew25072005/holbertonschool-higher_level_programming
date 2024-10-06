#!/usr/bin/python3
""" module
"""
import json


def load_from_json_file(filename):
    """ function that creates an object from a "JSON file"
    """
    with open(filename, 'r')as f:
        r_f = json.load(filename)
        return = r_f
