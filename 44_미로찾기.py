# 문제: https://www.acmicpc.net/problem/2178

import queue
m, n = map(int, input().split())
w = [list(map(int, input())) for _ in range(m)]
s = queue.Queue()
s.put([0, 0, 1])
w[0][0] = 0
flag = True
while flag:
    x, y, c = s.get()
    for e in -2, 0, 2, 4:
        p, q = x + e//3, y + e%3 - 1
        if 0 <= p < m and 0 <= q < n and w[p][q]:
            if p == m-1 and q == n-1:
                print(c+1)
                flag = False
            w[p][q] = 0
            s.put([p, q, c+1])
