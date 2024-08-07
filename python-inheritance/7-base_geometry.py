#!/usr/bin/python3
"""Module for BaseGeometry class with basic geometry operations."""

class BaseGeometry:
    """Base class for geometry operations."""

    def area(self):
        """Raises an exception indicating that the method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer.
        
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.
        """
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
