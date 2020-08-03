# https://www.acmicpc.net/problem/11404


"""
* 플로이드 와샬 알고리즘
    - 모든 정점에 대한 최단 거리를 구할 수 있음
    - n^3의 시간이 걸리므로 꼭 필요한 상황에서만 사용할 것
    - w[i][j]를 준비
    - i와 j가 같을 경우 0, 아닐 경우 float('inf')로 초기화
    - for k (0 ~ n): for i (0 ~ n): for j (0 ~ n):
        w[i][j] = min(w[i][j], w[i][k] + w[k][j])
"""

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
w = [[0 if i == j else float('inf') for j in range(n)] for i in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    w[a-1][b-1] = min(w[a-1][b-1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            w[i][j] = min(w[i][j], w[i][k] + w[k][j])

for p in w:
    print(*[0 if e == float('inf') else e for e in p])
