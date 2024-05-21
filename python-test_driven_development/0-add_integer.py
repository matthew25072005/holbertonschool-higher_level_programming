#!/usr/bin/python3

def add_integer(a, b=98):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, int) and isinstance(b, float):
        b = int(b)
        return a + b
    if isinstance(a, float) and isinstance(b, int):
        a = int(a)
        return a + b
    elif isinstance(a, float) and isinstance(b, float):
        a = int(a)
        b = int(b)
        return a + b
