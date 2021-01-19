# https://www.acmicpc.net/problem/7579


"""
dp[i][j] = 0 ~ i 까지 아이템과 j 비용을 이용하여 얻을 수 있는 최대 메모리
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
m = [*map(int, input().split())]
c = [*map(int, input().split())]
dp = [[0] * 10000 for _ in range(N)]
answer = float('inf')

dp[0][c[0]] = m[0]
for i in range(1, N):
    for j in range(10000):
        if c[i] <= j:
            dp[i][j] = dp[i-1][j-c[i]] + m[i]       # j - c[i] = i-1까지 c의 합
        dp[i][j] = max(dp[i][j], dp[i-1][j])

        if dp[i][j] >= M:
            answer = min(answer, j)

print(answer)