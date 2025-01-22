#!/usr/bin/python3
def element_at(my_list, idx):
    largo = len(my_list)
    if idx >= 0 and idx < largo:
        elemento = my_list[idx]
        print(f"Element at index {idx} is {elemento}")
    else:
        print(f"Element at index {idx} is None")