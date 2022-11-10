import sys
sys.setrecursionlimit(10000)


def recursion(m, n):
    if m == 0 or m == n:
        return 1
    return recursion(m, n-1) + recursion(m-1, n-1)


print(recursion(4, 12))
