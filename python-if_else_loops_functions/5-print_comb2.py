#!/usr/bin/python3
n = 0
while n >= 0 and n < 99:
    i = "{:02d}".format(n)
    char = str(i)
    print(str.format(char), end=", ")
    n += 1
if n == 99:
    char = str(n)
    print(str.format(char))