#!/usr/bin/python3
'''alx interview exercise'''


def minOperations(n):
    '''calculates the fewest number of operations
    needed to result in exactly n H'''
    if type(n) != int:
        return 0
    op = 0
    step = 2
    while (step <= n):
        if not (n % step):
            n = int(n / step)
            op += step
            step = 1
        step += 1
    return op
