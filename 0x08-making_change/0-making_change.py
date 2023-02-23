#!/usr/bin/python3
'''making changes'''


def makeChange(coins, total):
    '''determine the fewest number of coins needed to meet a given
    amount of total from a given pile of coins of different value'''
    if total <= 0:
        return 0
    add_coins = 0
    count = 0
    while add_coins <= total:
        if max(coins) > total or (max(coins) + add_coins) > total:
            coins.pop(coins.index(max(coins)))
        largest_coin = max(coins)
        add_coins += largest_coin
        count += 1
        if add_coins == total:
            return count
    return -1
