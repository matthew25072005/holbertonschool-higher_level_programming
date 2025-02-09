#!/usr/bin/python3
"""
This is a module
"""


class CountedIterator:
    """
    A class that wraps an iterator and counts the number of items iterated over.
    """

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        self.count += 1
        return next(self.iterator)

    def get_count(self):
        return self.count