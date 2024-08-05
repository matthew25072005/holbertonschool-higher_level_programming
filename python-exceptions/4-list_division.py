#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            # Intenta obtener los elementos de las listas
            elem1 = my_list_1[i]
            elem2 = my_list_2[i]

            # Intenta realizar la división
            try:
                result.append(elem1 / elem2)
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
            except TypeError:
                print("wrong type")
                result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        except Exception as e:
            print("An unexpected error occurred: {}".format(e))
            result.append(0)

    return result
