#!/usr/bin/python3
"""Matrix division function."""

def matrix_divided(matrix, div):
    """ 
    Divides all elements of a matrix by div.
    
    Args:
        matrix (list of lists): Matrix to divide (list of lists of integers/floats).
        div (int/float): The divisor.

    Returns:
        list of lists: A new matrix with elements divided by div.
    
    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats, 
                   if div is not a number, or if each row is not the same size.
        ZeroDivisionError: If div is 0.
    """

    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each element in the matrix is an integer or float
    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row has the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform the division and round the results to 2 decimal places
    return [[round(element / div, 2) for element in row] for row in matrix]
