# https://www.acmicpc.net/problem/2342


import sys

cost = [[2]*5 for _ in range(5)]
ddr = [*map(int, sys.stdin.readline().split())][:-1]
dp = [[[float('inf')]*5 for _ in range(5)] for _ in range(2)]
dp[0][0][0] = 0
check = [[i, j] for i in range(5) for j in range(5)]
s, t = 0, 1

for i in range(4):
    cost[i+1][i+1] = 1
    cost[i+1][(i-1)%4+1] = 3
    cost[i+1][(i+1)%4+1] = 3
    cost[i+1][(i+2)%4+1] = 4

for p in ddr:
    for l, r in check:
        if dp[s][l][r] != float('inf'):
            dp[t][p][r] = min(dp[t][p][r], dp[s][l][r] + cost[l][p])
            dp[t][l][p] = min(dp[t][l][p], dp[s][l][r] + cost[r][p])
    for l, r in check:
        dp[s][l][r] = float('inf')
    s, t = t, s

answer = min(map(lambda e: dp[s][e[0]][e[1]], check))
print(answer)