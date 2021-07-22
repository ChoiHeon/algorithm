# https://www.acmicpc.net/problem/2096


import sys
input = sys.stdin.readline

n = int(input())
a, b, c, d, e, f = [0] * 6

for _ in range(n):
    i, j, k = map(int, input().split())

    x = i + max(a, b)
    y = j + max(a, b, c)
    z = k + max(b, c)
    a, b, c = x, y, z

    x = i + min(d, e)
    y = j + min(d, e, f)
    z = k + min(e, f)
    d, e, f = x, y, z

print(max(a, b, c), min(d, e, f))