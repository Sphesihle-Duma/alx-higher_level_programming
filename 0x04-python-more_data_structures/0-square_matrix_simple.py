#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_matrix = matrix.copy()

    for i in range(len(matrix)):
        my_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (my_matrix)
