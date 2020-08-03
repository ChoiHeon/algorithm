# https://www.acmicpc.net/problem/10942


"""
* 다이나믹 프로그래밍 문제
    - dp[i][i] = True
    - dp[i][i+1] = (p[i] == p[i+1])
    - dp[i][j] (j - i >= 2) = (p[i] == p[j])  if dp[i+1][j-1] else (False)
"""

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
        dp[i][j] = dp[i+1][j-1] and (p[i] == p[j])      # and 의 연산순서를 이용하여 앞의 논리값을 조건으로 사용

for _ in range(int(input())):
    s, e = map(int, input().split())
    print(1 if dp[s][e] else 0)


