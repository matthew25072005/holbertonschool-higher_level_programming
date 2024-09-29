#!/usr/bin/python3
"""
Class BaseGeometry
Improved Geometry with Rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""superclass import """


class Rectangle(BaseGeometry):
    """
    Rectangle inheritated of BaseGometry got width and height
    """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height