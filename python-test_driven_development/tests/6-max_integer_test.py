#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_regular_list(self):
        """Test with a regular list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    def test_unsorted_list(self):
        """Test with an unsorted list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        """Test with a single element in the list."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        """Test with a list containing negative numbers."""
        self.assertEqual(max_integer([-1, -3, -2]), -1)

    def test_mixed_numbers(self):
        """Test with a list containing both positive and negative numbers."""
        self.assertEqual(max_integer([3, -2, 7, 1]), 7)

    def test_repeated_max(self):
        """Test with a list where the maximum number appears multiple times."""
        self.assertEqual(max_integer([1, 2, 2, 3, 3, 3]), 3)

    def test_large_numbers(self):
        """Test with large numbers."""
        self.assertEqual(max_integer([1000000, 5000000, 10000000]), 10000000)

    def test_floats(self):
        """Test with a list of floats."""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 2.0]), 3.5)

    def test_type_error(self):
        """Test that a TypeError is raised if the input is not a list."""
        with self.assertRaises(TypeError):
            max_integer("string")

if __name__ == "__main__":
    unittest.main()