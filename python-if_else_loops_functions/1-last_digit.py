#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ultimo_digito = abs(number)
last_digit = ultimo_digito % 10
if number < 0:
    if last_digit != 0:
        print("Last digit of",number,"is -"+str(last_digit),"and is less than 6 and not 0")
    elif last_digit == 0:
        print("Last digit of",number,"is",last_digit,"and is 0")
else:
    if last_digit % 10 > 5:
        print("Last digit of", number, "is " + str(last_digit),"and is greater than 5")
    elif last_digit % 10 < 6 and last_digit != 0:
        print("Last digit of", number, "is " + str(last_digit % 10),
        "and is less than 6 and not 0")
    elif last_digit % 10 == 0:
        print("Last digit of", number, "is", last_digit, "and is 0")
