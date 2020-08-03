# https://www.acmicpc.net/problem/2482


"""
* dp[i][j]: i개의 선형의 색상들 중, 제일 끝(오른쪽)의 색상을 j번 째로 선택하는 경우의 수
    - 최종적인 해는 원형을 고려하지만, 소단위 문제의 해는 선형이므로 처음부터 선형으로 해결한 후, 마지막에 원형을 고려
    - j번 째 색상을 칠하는 경우와 칠하지 않는 경우로 구분
    - 선형: dp[i][j] = 칠하는 경우 + 칠하지 않는 경우 = dp[i-2][j-1] + dp[i-1][j]  --> i < n
    - 원형: dp[n][k] = dp[n-3][k-1] + dp[n-1][k]
    - 일종의 확률과 통계 문제
"""

n = int(input())
k = int(input())
dp = [[0] * (k+1) for _ in range(n+1)]

for t in range(0, n+1):
    dp[t][0], dp[t][1] = 1, t

for i in range(2, n):
    for j in range(2, k+1):
        dp[i][j] = dp[i-1][j] + dp[i-2][j-1]

print((dp[n-1][k] + dp[n-3][k-1]) % 1000000003)