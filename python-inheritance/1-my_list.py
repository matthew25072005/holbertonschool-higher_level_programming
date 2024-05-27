#!/usr/bin/python3
"""A class MyList inherit a list"""


class MyList(list):
    """MyList class"""

    def print_sorted(self):
        print(sorted(self))
