#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))  # Intento de imprimir como entero
        return True
    except (ValueError, TypeError):  # Captura si no es posible formatear como entero
        return False
