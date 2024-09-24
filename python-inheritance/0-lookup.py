#!/usr/bin/python3
"""Module that defines a Rectangle"""


def lookup(obj):
    """
    Devuelve la lista de atributos y métodos disponibles de un objeto.

    Parámetros:
        obj: El objeto del cual obtener la lista de atributos y métodos.

    Retorna:
        list: Lista de atributos y métodos del objeto.
    """
    return dir(obj)
