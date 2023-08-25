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

    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1
