#!/usr/bin/python3
"""
This module defines a class named MyList.
"""


class MyList(list):
    """
    class mylist.
    """
    def print_sorted(self):
        """
        this funtion print a sorted list
        """
        print(sorted(self))
