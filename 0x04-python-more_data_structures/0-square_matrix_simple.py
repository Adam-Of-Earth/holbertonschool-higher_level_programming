#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    size = len(matrix[0])
    _matrix = [[x**2 for x in i] for i in matrix]
    return _matrix
