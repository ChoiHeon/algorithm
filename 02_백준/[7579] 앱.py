# https://www.acmicpc.net/problem/14238


"""
dp[k] = 비용 k 이하를 이용해 가질 수 있는 최대 메모리
dp[j] = max(dp[j], dp[j-cost[i]] + mem[i])
"""


n, m = map(int, input().split())
mem = [*map(int, input().split())]
cost = [*map(int, input().split())]
total_cost = sum(cost)
dp = [0] * (total_cost+1)

for i in range(n):
    for j in range(total_cost, cost[i]-1, -1):
        dp[j] = max(dp[j], dp[j-cost[i]] + mem[i])

for answer in range(total_cost+1):
    if dp[answer] >= m:
        print(answer)
        break
