#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = []
    for i in range(len(matrix)):
        squared = [(list(map((lambda x: x**2), matrix[i])))]
    return squared
