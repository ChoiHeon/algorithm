# https://www.acmicpc.net/problem/1005


import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    time = [*map(int, input().split())]
    graph = [[] for _ in range(n)]
    degree = [0] * n

    for __ in range(k):
        x, y = map(lambda e: int(e)-1, input().split())
        graph[x].append(y)
        degree[y] += 1

    goal = int(input())-1
    queue = deque()
    visited = set()
    answer = [-1] * n

    for i in range(n):
        if not degree[i]:
            queue.append(i)
            answer[i] = time[i]

    while queue:
        v = queue.popleft()
        if v == goal:
            break
        for u in graph[v]:
            degree[u] -= 1
        for u in graph[v]:
            answer[u] = max(answer[u], answer[v] + time[u])
            if not degree[u]:
                queue.append(u)

    print(answer[goal])

