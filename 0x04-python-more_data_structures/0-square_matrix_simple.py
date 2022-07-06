#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = []
    for elem in matrix:
        squared = [(list(map((lambda x: x**2), elem)))]
    return squared
