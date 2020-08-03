# https://www.acmicpc.net/problem/1932

import sys

i = sys.stdin.readline
N = int(i())
triangle = [ list(map(int, i().split())) for _ in range(N) ]

for i in range(1, N):
    triangle[i][0] += triangle[i-1][0]
    triangle[i][i] += triangle[i-1][i-1]
    for j in range(1, i):
        triangle[i][j] = max(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]

print(max(triangle[N-1]))

        


