#!/usr/bin/python3
"""Module that defines a Square"""


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
        self.size = size

    @property
    def size(self):
        """
        Getter para obtener el tamaño del lado del cuadrado.

        Retorna:
            int: El tamaño del lado del cuadrado.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter para definir el tamaño del lado del cuadrado.

        Parámetros:
            value (int): Nuevo tamaño del lado del cuadrado.

        Excepciones:
            TypeError: Si value no es un entero.
            ValueError: Si value es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calcula y retorna el área del cuadrado.

        Retorna:
            int: El área del cuadrado.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Imprime el cuadrado utilizando el carácter `#`.

        Si size es igual a 0, imprime una línea vacía.
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
