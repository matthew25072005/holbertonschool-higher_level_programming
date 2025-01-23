#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list1 = list(my_list)
    largo = len(list1)
    if idx >= 0 and idx < largo:
        list1[idx] = element
        return list1
    else:
        return my_list
