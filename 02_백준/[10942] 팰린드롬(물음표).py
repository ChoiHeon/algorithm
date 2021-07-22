import sys, math
input = sys.stdin.readline

n = int(input())
p = [-1] + [*map(int, input().split())]
dp = [[-1] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][i] = 1

for i in range(1, n):
    dp[i][i+1] = p[i] == p[i+1]

for diagonal in range(2, n):
    for i in range(1, n-diagonal+1):
        j = i + diagonal
        dp[i][j] = dp[i+1][j-1] and (p[i] == p[j])

for _ in range(int(input())):
    s, e = map(int, input().split())
    print(1 if dp[s][e] else 0)