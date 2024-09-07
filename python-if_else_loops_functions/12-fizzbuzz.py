#!/usr/bin/python3
def fizzbuzz():
    i = 0
    a = "Fizz"
    b = "Buzz"
    c = "FizzBuzz"
    while i <= 100:
        i += 1
        if i % 3 == 0 and i % 5 == 0:
            print("{} ".format(c), end="")
        elif i % 3 == 0:
            print("{} ".format(a), end="")
        elif i % 3 == 0 and i % 5 == 0:
            print("{} ".format(c), end="")
        else:
            print("{} ".format(i), end="")
