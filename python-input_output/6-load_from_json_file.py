#!/usr/bin/python3
"""
This is a module
"""
import json


def load_from_json_file(filename):
    with open(filename, 'w')as file:
        json.dump(data, file)
