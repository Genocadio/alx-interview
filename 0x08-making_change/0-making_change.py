#!/usr/bin/python3
'''Change calculator'''


def makeChange(coins, total):
    '''Return the minimum number of coins to make change for a given total'''
    if total <= 0:
        return 0

    current_total = 0
    changeCoins = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        r = (total - current_total) // coin
        current_total += r * coin
        changeCoins += r
        if current_total == total:
            return changeCoins
    return -1
