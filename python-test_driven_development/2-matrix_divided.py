#!/usr/bin/python3
"""Divide all elements of a matrix."""

def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a number.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int/float): The divisor.

    Returns:
        list of lists of float: A new matrix with all elements divided by div.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                    or if rows of matrix are not of the same size,
                    or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    # Check if matrix is a list of lists of integers/floats
    if not isinstance(matrix, list) or not matrix or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix is of the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number and not zero
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform the division and round to 2 decimal places
    return [[round(elem / div, 2) for elem in row] for row in matrix]
