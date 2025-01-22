#!/usr/bin/python3
def element_at(my_list, idx):
    if idx > 0 and my_list.index(idx):
        print("Element at index {:d} is {:d}".format(idx, element_at(list, idx)))