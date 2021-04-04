# https://www.acmicpc.net/problem/11049


n = int(input())
mat = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[float('inf')]*n for _ in range(n)]

for i in range(n):
    dp[i][i] = 0

for m in range(1, n):
    for i in range(n-m):
        j = i+m
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], mat[i][0]*mat[k][1]*mat[j][1] + dp[i][k] + dp[k+1][j])

print(dp[0][n-1])
