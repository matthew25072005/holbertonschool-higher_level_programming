#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_max_integer(self):
        """Test with positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_integer_negatives(self):
        """Test with negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_integer_mixed(self):
        """Test with positive and negative integers."""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_max_integer_single_element(self):
        """Test with a single element in the list."""
        self.assertEqual(max_integer([5]), 5)

    def test_max_integer_empty(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_max_integer_floats(self):
        """Test with a list of float numbers."""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_max_integer_strings(self):
        """Test with a list of strings, should raise TypeError."""
        with self.assertRaises(TypeError):
            max_integer(["1", "2", "3", "4"])

if __name__ == '__main__':
    unittest.main()
