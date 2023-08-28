#!/usr/bin/python3
"""
Makechage algorithm
"""


def makeChange(coins, total):
    """
    Create a list to store the minimum
    number of coins needed for each total
    """
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for i in coin:
            while(total >= i):
                counter += 1
                total -= i
        if total == 0:
            return counter
        return -1
