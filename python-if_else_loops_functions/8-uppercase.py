#!/usr/bin/python3
def uppercase(str):
    r = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            r += chr(ord(char) - 32)
        else:
            r += char
    print("{}".format(r))
