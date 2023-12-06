#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_mtx = []
    new_row = []
    for row in matrix:
        for item in row:
            new_row.append(item * item)
        new_mtx.append(new_row)
        new_row = []

    return new_mtx
