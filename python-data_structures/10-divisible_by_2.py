#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None

    for i in my_list:
        if i % 2 == 0:
            list_result.append(True)
            print("{} is divisible by 2".format(i))
        else:
            list_result.append(False)
            print("{} is not divisible by 2".format(i))

    return list_result 