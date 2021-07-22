# https://www.acmicpc.net/problem/1939


import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def check(s, e, w):
    visited = {s}
    queue = deque([s])
    while queue:
        v = queue.popleft()
        for u, l in graph[v]:
            if w <= l and u not in visited:
                if u == e:
                    return True
                visited.add(u)
                queue.append(u)
    return False


answer = 0
s, e = map(int, input().split())
l, h = 1, 1000000001
while l < h:
    m = (l+h)//2
    if check(s, e, m):
        answer = m
        l = m+1
    else:
        h = m
print(answer)