#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numberaux = abs(number)
l_d = numberaux % 10
if l_d == 0:
    print(f"Last digit of {number} is {l_d} and is 0")
elif l_d > 5:
    if number > 0:
        print(f"Last digit of {number} is {l_d} and is greater than 5")
    else:
        print(f"Last digit of {number} is -{l_d}\
        and is less than 6 and not 0")
else:
    if number > 0:
        print(f"Last digit of {number} is {l_d} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is -{l_d} and is less than 6 and not 0")
