#!/usr/bin/python3
"""Module that defines a Rectangle"""


class Rectangle:
    """
    Clase que define un rectángulo con atributos de ancho y altura.

    Atributos de clase:
        number_of_instances (int): Cuenta el número de instancias activas
        de la clase Rectangle.
        print_symbol: Símbolo usado para la representación en cadena del
        rectángulo.

    Atributos de instancia:
        __width (int): Ancho del rectángulo.
        __height (int): Altura del rectángulo.
    """

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter para obtener el ancho del rectángulo."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter para definir el ancho del rectángulo."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter para obtener la altura del rectángulo."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter para definir la altura del rectángulo."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcula y devuelve el área del rectángulo."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Calcula y devuelve el perímetro del rectángulo.
        Retorna 0 si el ancho o la altura es 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Devuelve una representación en cadena del rectángulo usando el
        carácter/símbolo almacenado en print_symbol. Retorna una cadena vacía
        si el ancho o la altura es 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(str(self.print_symbol) * self.__width
                         for _ in range(self.__height))

    def __repr__(self):
        """
        Devuelve una representación oficial del rectángulo que permite
        recrear la instancia utilizando eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Imprime un mensaje cuando la instancia del rectángulo es eliminada
        y decrementa el contador."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compara dos rectángulos y devuelve el más grande.

        Parámetros:
            rect_1 (Rectangle): Primer rectángulo.
            rect_2 (Rectangle): Segundo rectángulo.

        Excepciones:
            TypeError: Si alguno de los rectángulos no es una instancia de
            Rectangle.

        Retorna:
            Rectangle: El rectángulo más grande o rect_1 si son iguales.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Devuelve una nueva instancia de Rectangle donde el ancho y la
        altura son iguales a size.

        Parámetros:
            size (int, opcional): El tamaño del lado del cuadrado.
            Default es 0.

        Retorna:
            Rectangle: Nueva instancia de Rectangle.
        """
        return cls(size, size)
