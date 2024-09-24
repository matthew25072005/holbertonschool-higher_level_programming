#!/usr/bin/python3
"""
This module defines the MyList class that inherits from list
and includes a method to print the list sorted in ascending order.
"""


class MyList(list):
    """
    A subclass of list with an additional method to print the sorted list.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending order without modifying
        the original list.
        """
        print(sorted(self))
