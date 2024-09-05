#!/usr/bin/python3
def uppercase(c):
    result = ""
    for char in c:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
