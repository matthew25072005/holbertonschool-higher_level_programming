#!/usr/bin/python3
def uppercase(str):
    r = ""
    for char in str:
        if 'a' <= char <= 'z':
            r += chr(ord(char) - 32)
        else:
            r += char
    print(r)