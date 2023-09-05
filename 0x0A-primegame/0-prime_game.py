#!/usr/bin/python3
"""
Prime game with python
"""


def isWinner(x, nums):
    """
    Prime numbers game
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_available = [False] * (n + 1)

        for i in range(2, n + 1):
            if is_prime(i):
                prime_available[i] = True

        maria_turn = True
        while True:
            found_move = False
            for i in range(2, n + 1):
                if prime_available[i]:
                    prime = i
                    found_move = True
                    break

            if not found_move:
                break

            prime_available[prime] = False
            for i in range(prime, n + 1, prime):
                prime_available[i] = False

            if maria_turn:
                maria_wins += 1
            else:
                ben_wins += 1

            maria_turn = not maria_turn

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
