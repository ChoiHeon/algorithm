# https://www.acmicpc.net/problem/9252


a = [0] + [*input()]
b = [0] + [*input()]
n = len(a)
m = len(b)
dp = [[""]*m for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + a[i]
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(len(dp[-1][-1]))
print(dp[-1][-1])



