#!/usr/bin/python3
"""This module defines a CountedIterator class that tracks iterations."""

class CountedIterator:
    """An iterator that counts the number of items iterated over."""

    def __init__(self, iterable):
        """Initialize the CountedIterator with an iterable."""
        self.iterator = iter(iterable)  # Create an iterator from the iterable
        self.count = 0  # Initialize the counter

    def get_count(self):
        """Return the current count of items iterated."""
        return self.count

    def __next__(self):
        """Return the next item in the iterator and increment the count."""
        self.count += 1  # Increment the count
        return next(self.iterator)  # Return the next item from the original iterator

# Example usage
if __name__ == "__main__":
    data = [1, 2, 3, 4]
    counted_iter = CountedIterator(data)

    try:
        while True:
            item = next(counted_iter)
            print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
    except StopIteration:
        print("No more items.")
