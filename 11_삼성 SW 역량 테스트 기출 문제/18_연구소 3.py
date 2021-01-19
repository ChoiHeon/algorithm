# https://www.acmicpc.net/problem/17142


from itertools import combinations
from collections import deque


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
virus_pos = []
check = 0
answer = float('inf')

for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus_pos.append((i, j))
        if board[i][j] != 1:
            check += 1

for pos in combinations(virus_pos, m):
    dq = deque(pos)
    visited = set(pos)
    second = -1
    rest, cnt = len(virus_pos), 0

    while dq:
        for _ in range(len(dq)):
            x, y = dq.popleft()
            cnt += 1
            if board[x][y] == 2:
                rest -= 1
            if x > 0 and (x-1, y) not in visited and board[x-1][y] != 1:
                dq.append((x-1, y));    visited.add((x-1, y));
            if x < n-1 and (x+1, y) not in visited and board[x+1][y] != 1:
                dq.append((x+1, y));    visited.add((x+1, y))
            if y > 0 and (x, y-1) not in visited and board[x][y-1] != 1:
                dq.append((x, y-1));    visited.add((x, y-1))
            if y < n-1 and (x, y+1) not in visited and board[x][y+1] != 1:
                dq.append((x, y+1));    visited.add((x, y+1))
        second += 1
        if rest + cnt == check:
            cnt += rest
            break

    if check == cnt:
        answer = min(answer, second)

print(answer if answer != float('inf') else -1)


















