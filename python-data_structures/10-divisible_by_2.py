#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    list_1 = []
    for i in my_list:
        if i % 2 == 0:
            list_1.append(True)
            print("{} is divisible by 2".format(i))
        else:
            list_1.append(False)
            print("{} is not divisible by 2".format(i))

    return list_1
my_list = [1, 2, 3, 4]
divisible_by_2(my_list)
