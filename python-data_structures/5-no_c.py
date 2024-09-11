#!/usr/bin/python3
def no_c(my_string):
    result_chars = []
    min_c = "c"
    mayus_C = "C"
    for i in my_string:
        if i != min_c and i != mayus_C:
            result_chars.append(i)
    result_string = ''.join(result_chars)
    return result_string
