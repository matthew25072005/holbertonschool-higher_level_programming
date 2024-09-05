#!/usr/bin/python3
for i in range(9):
    f_n = i
    i += 1
    num = str(f_n) + str(i)
    if int(num) == 89:
        print("{}\n".format(num), end="")
    else:
        print("{}, ".format(num), end="")
    while i != 9:
        i += 1
        print("{}{}, ".format(f_n, i), end="")
