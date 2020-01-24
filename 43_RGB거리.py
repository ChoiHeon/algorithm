# 문제: https://www.acmicpc.net/problem/1149

w = [list(map(int, input().split())) for _ in range(int(input()))]
for i in range(1, len(w)):
    for j in range(3):
        w[i][j] += min(w[i-1][(j+1) % 3], w[i-1][(j+2) % 3])
print(min(w[-1]))

