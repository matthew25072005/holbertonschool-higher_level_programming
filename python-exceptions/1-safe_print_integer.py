#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Intentar imprimir el valor usando el formato entero
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        # Captura ValueError y TypeError si el valor no puede ser formateado como entero
        return False
