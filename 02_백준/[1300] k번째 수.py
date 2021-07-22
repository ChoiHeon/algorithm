# https://www.acmicpc.net/problem/1300

import numpy

n, k = map(int, input().split())
s, e = 1, n**2

while s < e:
    m = (s+e) // 2
    cnt = sum(map(lambda i: min(m//i, n), range(1, n+1)))

    if k <= cnt:
        e = m
    else:
        s = m+1

print(e)