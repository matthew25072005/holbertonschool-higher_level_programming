#!/usr/bin/python3
def fizzbuzz():
    i = 0
    a = Fizz
    b = Buzz
    while i < 100:
        i += 1
        if i % 3 == 0:
            print("{} ".format(a))
        elif i % 5 == 0:
            print("{} ".format(b))
        else:
            print("{} ".format(i))
