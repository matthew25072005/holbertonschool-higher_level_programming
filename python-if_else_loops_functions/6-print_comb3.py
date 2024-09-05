#!/usr/bin/python3
for i in range(9):
    f_n = i
    i += 1
    num = str(f_n) + str(i)
    print("{}, ".format(num), end="")
    while i != 9:
        i += 1
        print("{}{}, ".format(f_n, i), end="")
