#!/usr/bin/python3

def isWinner(x, nums):
    """
    :type x: int
    :type nums: List[int]
    :rtype: str
    """
    if x <= 0 or nums is None or x != len(nums):
        return None

    ben, maria = 0, 0
    a = [1 for _ in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0

    sieve_of_eratosthenes(a)

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    return "Ben" if ben > maria else "Maria" if maria > ben else None


def sieve_of_eratosthenes(a):
    """ Returns a list of prime numbers from 0 to n """
    for i in range(2, len(a)):
        remove_multiples(a, i)


def remove_multiples(ls, x):
    """
    :type ls: List[int]
    :type x: int
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
