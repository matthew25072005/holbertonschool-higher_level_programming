#!/usr/bin/python3
n1 = 0
n2 = 1
i = 10

while n2 <= i and n1 < 9:
    print(f"{n1}{n2}" + (", " if not (n1 == 8 and n2 == 9) else ""), end="")
    n2 += 1
    if n2 == i and n1 < 9:
        n1 += 1
        n2 = n1 + 1