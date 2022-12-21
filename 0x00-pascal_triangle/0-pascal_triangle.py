#!/usr/bin/python3
'''pascal triangle '''


def pascal_triangle(n):
    '''return a lists of integers representing pascal's
    triangle of n'''
    pasc_list = []
    if n <= 0:
        return pascal_list
    for i in range(n):
        triangle = []
        for j in range(i + 1):
            if j == 0 or j == i:
                triangle.append(1)
            elif i > 0 and j > 0:
                triangle.append(pasc_list[i - 1][j - 1] + pasc_list[i - 1][j])
        pasc_list.append(triangle)
    return pasc_list
