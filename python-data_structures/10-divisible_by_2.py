#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None

    num = my_list[0]
    for i in my_list:
        if i % 2 == 0:
            num = i
            print("{} is divisible by 2".format(num))
        else:
            print("{} is not divisible by 2".format(num))
