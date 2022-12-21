#!/usr/bin/python3
'''pascal triangle '''


def pascal_triangle(n):
    '''return a lists of integers representing pascal's
    triangle of n'''
    pascal_list = []
    if n <= 0:
        return pascal_list
    for i in range(n):
        triangle = []
        for j in range(i + 1):
            if j == 0 or j == i:
                triangle.append(1)
            elif i > 0 and j > 0:
                triangle.append(pascal_list[i - 1][j - 1] + pascal_list[i - 1][j])
        pascal_list.append(triangle)
    return pascal_list
