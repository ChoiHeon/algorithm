# https://www.acmicpc.net/problem/2294

n, k = map(int, input().split())
coins = {int(input()) for _ in range(n)}
coins = sorted(coins)
dp = [0] + [float('inf')] * k

for coin in coins:
    for i in range(k+1):
        if coin <= i:
            dp[i] = min(dp[i], dp[i-coin]+1)

print(dp[-1] if dp[-1] != float('inf') else -1)