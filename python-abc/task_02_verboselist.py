#!/usr/bin/python3
"""This module defines a VerboseList class that extends the built-in list class."""

class VerboseList(list):
    """A list subclass that provides verbose output for operations."""

    def append(self, item):
        """Add an item to the list with a notification."""
        super().append(item)  # Call the original append method
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list with items from an iterable with a notification."""
        count = len(iterable)
        super().extend(iterable)  # Call the original extend method
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove an item from the list with a notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)  # Call the original remove method

    def pop(self, index=-1):
        """Pop an item from the list with a notification."""
        item = super().pop(index)  # Call the original pop method
        print(f"Popped [{item}] from the list.")
        return item  # Return the popped item

# Example usage
if __name__ == "__main__":
    vl = VerboseList([1, 2, 3])
    vl.append(4)
    vl.extend([5, 6])
    vl.remove(2)
    vl.pop()
    vl.pop(0)
