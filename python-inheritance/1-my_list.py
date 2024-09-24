#!/usr/bin/python3
"""Module that defines a Rectangle"""


class MyList(list):
    """
    MyList es una clase que hereda de la clase integrada list.
    """

    def print_sorted(self):
        """
        Método que imprime la lista en orden ascendente, pero no modifica la lista original.
        """
    sorted(self)
    print(self)
