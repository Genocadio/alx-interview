#!/usr/bin/python3
"""N queens problem"""
import sys


def nqueens(n, j, list):
    """N queens problem"""
    for i in range(n):
        cache = 0
        for b in list:
            if i == b[1]:
                cache = 1
                break
            if j - i == b[0] - b[1]:
                cache = 1
                break
            if i - b[1] == b[0] - j:
                cache = 1
                break
        if cache == 0:
            list.append([j, i])
            if j != n - 1:
                nqueens(n, j + 1, list)
            else:
                print(list)
            list.pop()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    list = []
    nqueens(n, 0, list)
