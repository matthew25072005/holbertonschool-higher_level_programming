#!/usr/bin/python3
"""Modules that defines a Square"""


class Square:
    """
    Esta clase representa un cuadrado.

    Atributos:
        __s (int): Tamaño del lado del cuadrado.
    """

    def __init__(self, size):
        """
        Inicializa una instancia de la clase Square.

        Parámetros:
            s (int): Tamaño del lado del cuadrado.

        Nota:
            El tamaño del lado se almacena en un atributo privado __s.
        """
        self.__size = size
