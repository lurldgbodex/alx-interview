#!/usr/bin/python3
'''alx interview'''


def rotate_2d_matrix(matrix):
    '''rotate a n x n 2D matrix to 90 degrees clockwise'''
    len_matrix = len(matrix[0])
    start = len_matrix - 1
    stop = -1
    step = -1
    for row in range(start, stop, step):
        for col in range(0, len_matrix):
            matrix[col].append(matrix[row].pop(0))
