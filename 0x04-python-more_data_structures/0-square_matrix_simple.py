#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            squared.append(list(map((lambda x: x**2), matrix[i])))
            break
    return squared
