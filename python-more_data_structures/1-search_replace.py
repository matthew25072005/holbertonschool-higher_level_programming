#!/usr/bin/python3
#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list1 = my_list[:]
    for idx, i in enumerate(my_list):
        if i == search:
            list1[idx] = replace
    return list1
