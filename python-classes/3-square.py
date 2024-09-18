#!/usr/bin/python3
"""Modules that defines a Square"""


class Square:
    """
    Define un cuadrado con un tamaño opcional.

    Atributos:
        __size (int): Tamaño del lado del cuadrado.
    """

    def __init__(self, size=0):
        """
        Inicializa una instancia de la clase Square.

        Parámetros:
            size (int, opcional): Tamaño del lado del cuadrado. Default es 0.

        Excepciones:
            TypeError: Si size no es un entero.
            ValueError: Si size es menor que 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """
        Calcula y retorna el área del cuadrado.

        Retorna:
            int: El área del cuadrado.
        """
        return self.__size * self.__size
