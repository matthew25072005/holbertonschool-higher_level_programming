#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ultimo_digito = abs(number)
if number < 0:
    if ultimo_digito % 10 > 5:
        print("Last digit of", number, "is -" + str(ultimo_digito % 10) ,"and is greater than 5")
    elif ultimo_digito % 10 < 6 and ultimo_digito % 10 != 0:
        print("Last digit of", number, "is -" + str(ultimo_digito % 10) , "and is less than 6 and not 0")
    elif ultimo_digito % 10 == 0:
        print ("Last digit of", number, "is", ultimo_digito % 10, "and is 0")
else:
    if ultimo_digito % 10 > 5:
        print("Last digit of", number, "is " + str(ultimo_digito % 10) ,"and is greater than 5")
    elif ultimo_digito % 10 < 6 and ultimo_digito % 10 != 0:
        print("Last digit of", number, "is " + str(ultimo_digito % 10) , "and is less than 6 and not 0")
    elif ultimo_digito % 10 == 0:
        print ("Last digit of", number, "is", ultimo_digito % 10, "and is 0")
