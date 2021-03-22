# https://www.acmicpc.net/problem/2579


"""
* 정의
dp[i][0]: 한 칸을 올라서 i 번째 계단에 도착했을 때 최대 값
dp[i][1]: 두 칸을 올라서 i 번째 계단에 도착했을 때 최대 값

* 초기화
dp[0] = [stair[0], 0]
dp[1] = [stair[0] + stair[1], stair[1]]

* 점화식
dp[i][0] = dp[i-1][1] + stair[i]
dp[i][1] = max(dp[i-2]) + stair[i]
"""


n = int(input())
stair = [int(input()) for _ in range(n)]
dp = [[stair[i], stair[i]] for i in range(n)]

if n < 3:
    print(sum(stair))
else:
    dp[0][1] = 0
    dp[1][0] += stair[0]

    for i in range(2, n):
        dp[i][0] += dp[i-1][1]
        dp[i][1] += max(dp[i-2])

    print(max(dp[n-1]))

# dp 출력
for i in range(2):
    for j in range(n):
        print("{:3}".format(dp[j][i]), end=' ')
    print()
