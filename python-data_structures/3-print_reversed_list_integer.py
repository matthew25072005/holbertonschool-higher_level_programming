#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for elemento in list(reversed(my_list)):
        print("{:d}".format(elemento))
