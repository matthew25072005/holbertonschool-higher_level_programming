#!/usr/bin/python3
i = 0
while i >= 0 and i < 99:
    char = str(i)
    print(str.format(char), end=", ")
    i += 1
if i == 99:
    char = str(i)
    print(str.format(char))
