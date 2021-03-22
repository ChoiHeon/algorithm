# https://www.acmicpc.net/problem/13913


import sys
from collections import deque
sys.setrecursionlimit(10**6)

LIMIT = 100000
n, k = map(int, input().split())
dq = deque([n])
dist = [-1] * (LIMIT + 1)
visited = [0] * (LIMIT + 1)
visited[n] = 1

while dq[0] != k:
    x = dq.popleft()
    for y in [x-1, x+1, x*2]:
        if 0 <= y <= LIMIT and not visited[y]:
            dist[y] = x
            visited[y] = 1
            dq.append(y)


def print_answer(x, t):
    if dist[x] == -1:   print(t)
    else:               print_answer(dist[x], t+1)
    print(x, end=' ')


print_answer(k, 0)