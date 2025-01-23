#!/usr/bin/python3
def no_c(my_string):
    frase = []
    for i in my_string:
        char = ord(i)
        if char == 99 or char == 67:
            char += 1
        else:
            frase.append(i)
            char += 1
    return ''.join(frase)