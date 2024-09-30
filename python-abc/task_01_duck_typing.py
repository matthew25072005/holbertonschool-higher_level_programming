#!/usr/bin/env python3

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Clase abstracta para definir la interfaz de las formas."""

    @abstractmethod
    def area(self):
        """Método abstracto para calcular el área de la forma."""
        pass

    @abstractmethod
    def perimeter(self):
        """Método abstracto para calcular el perímetro de la forma."""
        pass


class Circle(Shape):
    """Clase que representa un círculo."""

    def __init__(self, radius):
        """Inicializa el círculo con un radio dado.

        Args:
            radius (float): El radio del círculo.
        """
        self.radius = radius  # Permitir radio negativo

    def area(self):
        """Calcula y devuelve el área del círculo."""
        return math.pi * (self.radius ** 2) if self.radius >= 0 else 0

    def perimeter(self):
        """Calcula y devuelve el perímetro del círculo."""
        return 2 * math.pi * self.radius if self.radius >= 0 else 0


class Rectangle(Shape):
    """Clase que representa un rectángulo."""

    def __init__(self, width, height):
        """Inicializa el rectángulo con un ancho y alto dados.

        Args:
            width (float): El ancho del rectángulo.
            height (float): El alto del rectángulo.
        """
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative numbers.")
        self.width = width
        self.height = height

    def area(self):
        """Calcula y devuelve el área del rectángulo."""
        return self.width * self.height

    def perimeter(self):
        """Calcula y devuelve el perímetro del rectángulo."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Imprime el área y el perímetro de una forma dada.

    Args:
        shape (Shape): Una instancia de una clase que hereda de Shape.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
