#!/usr/bin/python3
'''making changes'''


def makeChange(coins, total):
    '''determine the fewest number of coins needed to meet a given
    amount of total from a given pile of coins of different value'''
    if total <= 0:
        return 0
    count = 0
    index = 0
    coin_length = len(coins)
    sort_coin = sorted(coins, reverse=True)
    while total > 0:
        if index >= coin_length:
            return -1
        if total - sort_coin[index] >= 0:
            total -= sort_coin[index]
            count += 1
        else:
            index += 1
    return count
