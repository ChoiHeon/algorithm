# https://www.acmicpc.net/problem/2176


import sys, heapq
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
dp = [-1] * (n+1)
s, t= 1, 2

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

dist = [float('inf')] * (n+1)
dist[t] = 0
heap = [[dist[t], t]]
while heap:
    c1, v1 = heapq.heappop(heap)
    if c1 < dist[v1]:
        continue
    for c2, v2 in graph[v1]:
        if c1 + c2 < dist[v2]:
            dist[v2] = c1 + c2
            heapq.heappush(heap, [dist[v2], v2])


def dfs(v):
    if v == t:
        return 1
    if dp[v] != -1:
        return dp[v]

    dp[v] = 0
    for _, u in graph[v]:
        if dist[v] > dist[u]:
            dp[v] += dfs(u)
    return dp[v]


print(dfs(s))
