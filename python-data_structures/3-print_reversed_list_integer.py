#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    lista_invertida = list(reversed(my_list))
    for elemento in lista_invertida:
        print("{}".format(elemento))
