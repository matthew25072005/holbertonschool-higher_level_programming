#!/usr/bin/python3
i = 97
while i > 96 and i < 123:
    char = chr(i)
    print(str.format(char), end="")
    i += 1
    if i == 101 or i == 113:
        i += 1
