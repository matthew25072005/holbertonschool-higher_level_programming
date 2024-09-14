#!/usr/bin/python3
"""
This module defines a function to divide all elements of a matrix by a given number.
"""

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number and round to 2 decimal places.

    Args:
        matrix (list of list of integers/floats): The matrix to be divided.
        div (int/float): The number by which to divide each element of the matrix.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats, if rows are not of the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.

    Returns:
        list of list of floats: A new matrix with each element divided by div and rounded to 2 decimal places.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_length = None
    for row in matrix:
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    
    return new_matrix
