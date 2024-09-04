#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
ldo = "Last digit of"
if number < 0 and ld != 0:
    print(ldo, number, "is", ld * -1, "and is less than 6 and not 0")
else:
    if ld > 5:
        print(ldo, number, "is", ld, "and is greater than 5")
    elif ld < 6 and ld != 0:
        print(ldo, number, "is ", ld, "and is less than 6 and not 0")
    elif ld == 0:
        print(ldo, number, "is", ld, "and is 0")
