#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        num = []
        for i in row:
            num.append("{:d}".format(i))
        print(" ".join(num))
