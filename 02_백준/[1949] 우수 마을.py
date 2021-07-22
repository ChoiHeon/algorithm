# https://www.acmicpc.net/problem/1949


import sys
sys.setrecursionlimit(10**6)

n = int(input())
p = [*map(int, input().split())]
e = [[] for _ in range(n)]
visited = [False] * n
dp = [[0, 0] for _ in range(n)]

for _ in range(n-1):
    a, b = map(lambda x: int(x)-1, input().split())
    e[a].append(b)
    e[b].append(a)


def sol(i):
    visited[i] = True
    dp[i][1] = p[i]
    for j in e[i]:
        if visited[j]:
            continue
        sol(j)
        dp[i][0] += max(dp[j])
        dp[i][1] += dp[j][0]


sol(0)
print(max(dp[0]))




