#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end=' ')
                count += 1
    except IndexError:
        # Si ocurre IndexError, significa que hemos llegado al final de la lista
        pass
    print()  # Para finalizar la línea después de imprimir todos los enteros
    return count
