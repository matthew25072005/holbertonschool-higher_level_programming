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
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, int) and isinstance(b, float):
        b = int(b)
        return a + b
    if isinstance(a, float) and isinstance(b, int):
        a = int(a)
        return a + b
    elif isinstance(a, float) and isinstance(b, float):
        a = int(a)
        b = int(b)
        return a + b
