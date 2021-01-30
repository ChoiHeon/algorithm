# https://www.acmicpc.net/problem/17404


"""
    * dp[i][j]
        - 1 ~ i까지 색을 칠함
        - 마지막 집의 색
        - 최소값을 저장

    * k
        - 첫번 째 집의 색을 의미함
        - 나머지 색깔을 칠한 경우 값을 무한대로 초기화
        - 마지막에 최소값을 구할 때 첫번 째 집의 색을 제외하고 비교
"""


import sys
read = sys.stdin.readline

n = int(read())
h = [[*map(int, read().split())] for _ in range(n)]
dp = [[0]*3 for _ in range(n)]
ans = float('inf')

for k in range(3):
    for l in range(3):
        if k == l:
            dp[0][l] = h[0][l]
        else:
            dp[0][l] = float('inf')

    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + h[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + h[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + h[i][2]

    for m in range(3):
        if m != k:
            ans = min(ans, dp[-1][m])

print(ans)