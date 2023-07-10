#!/usr/bin/python3
"""
Minimum operation function
"""


def minOperations(n):
    """
    Returns the minimum number of operations needed
    to achieve n H characters in the file.

    Args:
    - n: An integer representing the desired number of H characters.

    Returns:
    - An integer representing the minimum number of operations.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1

    return operations
