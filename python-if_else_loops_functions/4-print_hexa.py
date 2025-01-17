#!/usr/bin/python3
i = 0
while i >= 0 and i < 99:
    char = str(i)
    print(f"{str.format(char)} = {hex(i)}")
    i += 1
