#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Suma dos números enteros o flotantes y devuelve el resultado como un entero.

    Args:
        a (int or float): Primer número.
        b (int or float, optional): Segundo número (por defecto es 98).

    Returns:
        int: Suma de a y b como un entero.
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return int(a) + int(b)
    else:
        raise TypeError("Ambos argumentos deben ser enteros o flotantes")

# Ejemplo de uso
resultado = add_integer(1, 2)
