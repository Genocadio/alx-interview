#!/usr/bin/python3
"""Prime game module"""


def isWinner(x, nums):
    """Check if a number is a winner"""
    def sieve_of_eratosthenes(n):
        """Sieve of Eratosthenes"""
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        return [i for i in range(n + 1) if primes[i]]

    def can_win(n):
        """Check if a number can win"""
        primes = sieve_of_eratosthenes(n)
        maria_turn = True
        while n > 1:
            found_prime = False
            for prime in primes:
                if n % prime == 0:
                    n -= prime
                    found_prime = True
                    break
            if not found_prime:
                break
            maria_turn = not maria_turn
        return maria_turn

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if can_win(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
