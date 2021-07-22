# https://www.acmicpc.net/problem/1717

"""
Union Find 를 구현하는 문제
"""


import sys

sys.setrecursionlimit(10**6)
parents = []


def get_parent(x):
    global parents
    if parents[x] == x:
        return x
    parents[x] = get_parent(parents[x])
    return parents[x]


def union(x, y):
    global parents
    a = get_parent(x)
    b = get_parent(y)
    parents[a] = b


def find(x, y):
    a = get_parent(x)
    b = get_parent(y)
    return a == b


i = sys.stdin.readline
n, m = map(int, i().split())
parents = list(range(n+1))

for _ in range(m):
    op, x, y = map(int, i().split())
    if op:
        print("YES") if find(x, y) else print("NO")
    else:
        union(x, y)

