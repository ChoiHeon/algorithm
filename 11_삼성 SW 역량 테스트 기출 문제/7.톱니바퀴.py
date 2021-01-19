# https://www.acmicpc.net/workbook/view/1152
# https://www.acmicpc.net/problem/14891

from collections import deque


gears = [deque(map(int, input())) for _ in range(4)]
rotate = [0] * 4

for _ in range(int(input())):
    k, dir = map(int, input().split())
    k -= 1

    for i in range(4):
        rotate[i] = int(gears[i][2] != gears[i+1][6]) if i < k else int(gears[i-1][2] != gears[i][6])
    rotate[k] = dir
    for i in range(k+1, 4):
        rotate[i] = rotate[i] * rotate[i-1] * -1
    for i in range(k-1, -1, -1):
        rotate[i] = rotate[i] * rotate[i+1] * -1

    for i in range(4):
        if rotate[i] == 1:
            gears[i].appendleft(gears[i].pop())
        elif rotate[i] == -1:
            gears[i].append(gears[i].popleft())

print(sum([gears[i][0] * (2 ** i) for i in range(4)]))



