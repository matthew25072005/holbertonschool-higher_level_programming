#!/usr/bin/python3
i = 97
while i > 96 and i < 123:
    char = chr(i)
    print(str.format(char), end="")
    i += 1
