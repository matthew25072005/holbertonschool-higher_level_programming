#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None

    num = my_list[0]
    for i in my_list:
        if i % 2 == 0:
            num = i
            print(num)
