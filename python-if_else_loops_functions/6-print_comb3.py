#!/usr/bin/python3
n1 = 0
n2 = 1
i = 10

while n2 <= i and n1 < 9:
    if n1 == 8:
        print(f"{n1}{n2}")
    else:
        print(f"{n1}{n2}", end=", ")
    n2 += 1
    if n2 == i and n1 < 9:
        n1 += 1
        n2 = n1 + 1

