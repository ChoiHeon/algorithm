# https://www.acmicpc.net/problem/11049
# 이 문제는 파이썬으로 실행 시 시간초과 발생
# 문제 유형: dynamic programming
# 특징: 이차원 배열을 대각선 순서대로 채워나가야 한다. 이를 위해 for문의 코드를 응용해야 한다
# dp[i][j] = i번 째 행렬부터 j번째 행렬까지 최소 행렬연산 횟수
import sys

i  = sys.stdin.readline
n = int(i())
m = [list(map(int, i().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]


for diag in range(1, n):
    for i in range(n-diag):
        j = i+diag
        dp[i][j] = sys.maxsize
        for k in range(i,j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + m[i][0]*m[k][1]*m[j][1])

print(dp[0][n-1])