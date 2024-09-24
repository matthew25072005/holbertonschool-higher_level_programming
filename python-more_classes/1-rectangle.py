#!/usr/bin/python3
"""Module that defines a Rectangle"""


class Rectangle:
    """
    Clase que define un rectángulo con atributos de ancho y altura.

    Atributos:
        __width (int): Ancho del rectángulo.
        __height (int): Altura del rectángulo.
    """

    def __init__(self, width=0, height=0):
        """
        Inicializa una instancia de la clase Rectangle.

        Parámetros:
            width (int, opcional): Ancho del rectángulo. Default es 0.
            height (int, opcional): Altura del rectángulo. Default es 0.

        Excepciones:
            TypeError: Si width o height no son enteros.
            ValueError: Si width o height son menores que 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter para obtener el ancho del rectángulo.

        Retorna:
            int: El ancho del rectángulo.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter para definir el ancho del rectángulo.

        Parámetros:
            value (int): Nuevo ancho del rectángulo.

        Excepciones:
            TypeError: Si value no es un entero.
            ValueError: Si value es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter para obtener la altura del rectángulo.

        Retorna:
            int: La altura del rectángulo.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter para definir la altura del rectángulo.

        Parámetros:
            value (int): Nueva altura del rectángulo.

        Excepciones:
            TypeError: Si value no es un entero.
            ValueError: Si value es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value