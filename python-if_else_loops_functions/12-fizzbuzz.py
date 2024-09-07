#!/usr/bin/python3
def fizzbuzz():
    i = 0
    while i < 100:
        i += 1
        if i % 3 == 0:
            print("Fizz ".format)
        elif i % 5 == 0:
            print("Buzz ".format)
        else:
            print("{} ".format(i))
