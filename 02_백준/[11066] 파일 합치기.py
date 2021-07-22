# https://www.acmicpc.net/problem/11066


"""
* 동적 계획법
    - 수열의 부분합을 반복 계산해야 하므로 아래의 방법으로 미리 부분합을 저장해늫는다
    - 수열 P에 대하여 Q[i] = P[i] + P[i-1]을 이용해 수열 Q를 생성
    - P[i] ~ P[j]의 부분합은 Q[j] - Q[i-1]로 쉽게 구할 수 있다

    - 점화식 세우기가 가장 어려웠음
    - dp[i][j] = min(dp[i][k] + do[k+1][j] + Q[j] - Q[i-1]) (i <= k < j)
"""

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    w = [0]
    for e in [*map(int, input().split())]:
        w.append(w[-1]+e)

    dp = [[0]*(n+1) for _ in range(n+1)]

    for diagonal in range(1, n):
        for i in range(1, n-diagonal+1):
            j = i + diagonal
            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + w[j] - w[i-1])
    print(dp[1][n])