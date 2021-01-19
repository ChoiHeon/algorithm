# https://www.acmicpc.net/problem/1520


"""
* 메모이제이션
    - dp[i][j]를 -1로 초기화
    - 이후 해당 좌표를 탐색할 경우 0이상의 값으로 변경함으로써
    - 방문 여부를 알 수 있음
"""

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

m, n = map(int, input().split())
w = []

for _ in range(m):
    w.append(list(map(int, input().split())))

dp = [[-1] * n for _ in range(m)]       # 0으로 초기화 할 경우 시간초과 발생
dp[m-1][n-1] = 1


def dfs(i, j):
    global dp

    if dp[i][j] != -1:
        return dp[i][j]

    ret = 0
    if i > 0 and w[i][j] > w[i - 1][j]:         # up
        ret += dfs(i - 1, j)
    if i < m - 1 and w[i][j] > w[i + 1][j]:     # down
        ret += dfs(i + 1, j)
    if j > 0 and w[i][j] > w[i][j - 1]:         # left
        ret += dfs(i, j - 1)
    if j < n - 1 and w[i][j] > w[i][j + 1]:     # right
        ret += dfs(i, j + 1)
    dp[i][j] = ret

    return dp[i][j]


print(dfs(0, 0))