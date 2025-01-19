#!/usr/bin/python3
n1 = 0
n2 = 1
i = 10
while n2 <= i and n1 < 9:
    char1 = str(n1)
    char2= str(n2)
    if n1 == 8:
        print(str.format(char1) + str.format(char2))
    else:
        print(str.format(char1) + str.format(char2), end=", ")
    n2 += 1
    if n2 == i and n1 < 9:
        n1 += 1
        n2 = n1 + 1
