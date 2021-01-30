# https://www.acmicpc.net/problem/2293

import sys

i = sys.stdin.readline
n, k = list(map(int, i().split()))
c = sorted([int(i()) for _ in range(n)])
dp = [[0]*(k+1) for _ in range(2)]
dp[0][0] = 1

for i in range(1, n+1):
    for j in range(k+1):
        if c[i-1] > j:
            dp[1][j] = dp[0][j]
        else:
            dp[1][j] = dp[0][j] + dp[1][j - c[i - 1]]
    dp[0] = dp[1]

print(dp[1][k])