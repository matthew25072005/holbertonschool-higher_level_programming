#!/usr/bin/python3

def no_c(my_string):
    c = "c"
    c_mayus = "C"
    new_string = ''.join ([i for i in my_string if i != c and i != c_mayus:])
    return new_string
