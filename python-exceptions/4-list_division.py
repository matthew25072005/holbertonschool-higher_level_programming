#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []  # Initialize an empty list to store the results
    for i in range(list_length):
        try:
            result_list.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            result_list.append(0)
            print("division by 0")
        except TypeError:
            result_list.append(0)
            print("wrong type")
        except IndexError:
            result_list.append(0)
            print("out of range")
        finally:
            pass
    return result_list
