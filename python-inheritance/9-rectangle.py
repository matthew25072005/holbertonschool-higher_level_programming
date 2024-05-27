#!/usr/bin/python3
"""9-rectangle.py: A Rectangle class inheriting from BaseGeometry with added perimeter method."""

# Import the BaseGeometry class from the 7-base_geometry module
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A class representing a rectangle with a given width and height.

    Inherits from the BaseGeometry class.
    """

    def __init__(self, width, height):
        """Initialize the rectangle with the given width and height.

        Validates the width and height using the integer_validator method
        from the BaseGeometry class.

        :param width: The width of the rectangle as an integer.
        :param height: The height of the rectangle as an integer.
        """
        super().integer_validator('width', width)  # Validate the width
        self.__width = width  # Set the width
        super().integer_validator('height', height)  # Validate the height
        self.__height = height  # Set the height

    def area(self):
        """Return the area of the rectangle.

        Calculates the area by multiplying the width and height.

        :return: The area of the rectangle as an integer.
        """
        return self.__width * self.__height  # Calculate the area

    def perimeter(self):
        """Return the perimeter of the rectangle.

        Calculates the perimeter by adding the width and height twice.

        :return: The perimeter of the rectangle as an integer.
        """
        return 2 * (self.__width + self.__height)  # Calculate the perimeter

    def __str__(self):
        """Return a string representation of the rectangle.

        :return: A string in the format '[Rectangle] width/height'.
        """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)  # Return the string representation