#!/usr/bin/python3
"""
serialize and save to file
and load and deserialize
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes data in JSON format and saves it to a file.

    Arguments:
    data: The data to be serialized.
    filename (str): The name of the file
    where the data will be saved.
    """
    with open(filename, "w") as write_file:
        json.dump(data, write_file)


def load_and_deserialize(filename):
    """
    Loads data from a file and deserializes it from JSON format.

    Args:
    filename (str): The name of the file from which the data will be loaded.

    Returns:
    The data deserialized from the JSON file.
    """
    with open(filename, "r") as read_file:
        data = json.load(read_file)
    return data