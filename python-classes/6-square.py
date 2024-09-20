#!/usr/bin/python3
"""Module that defines a Square"""


class Square:
    """
    Define un cuadrado con tamaño y posición opcionales.

    Atributos:
        __size (int): Tamaño del lado del cuadrado.
        __position (tuple): Posición en la impresión, representada por un espacio (x, y).
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Inicializa una instancia de la clase Square.

        Parámetros:
            size (int, opcional): Tamaño del lado del cuadrado. Default es 0.
            position (tuple, opcional): Posición para imprimir el cuadrado.
            Default es (0, 0).

        Excepciones:
            TypeError: Si size no es un entero, o position no es una tupla de
            2 enteros positivos.
            ValueError: Si size es menor que 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter para obtener la posición de impresión del cuadrado.

        Retorna:
            tuple: La posición (x, y) para imprimir el cuadrado.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter para definir la posición de impresión del cuadrado.

        Parámetros:
            value (tuple): Nueva posición (x, y).

        Excepciones:
            TypeError: Si value no es una tupla de 2 enteros positivos.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
           not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calcula y retorna el área del cuadrado.

        Retorna:
            int: El área del cuadrado.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Imprime el cuadrado utilizando el carácter `#` con base en la posición y el tamaño.

        Si size es igual a 0, imprime una línea vacía.
        """
        if self.__size == 0:
            print("")
        else:
            # Imprimir las líneas en blanco según position[1]
            for y in range(self.__position[1]):
                print("")

            # Imprimir el cuadrado con los espacios de position[0]
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
