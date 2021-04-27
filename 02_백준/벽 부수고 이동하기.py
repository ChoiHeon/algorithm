# https://www.acmicpc.net/problem/2206


import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[[float('inf')]*2 for _ in range(m)] for __ in range(n)]
visited[0][0][0] = 1
queue = deque()
queue.append((0, 0, 0))

while queue:
    x, y, f = queue.popleft()
    if x == n-1 and y == m-1:
        print(visited[-1][-1][f])
        break
    for dx, dy in dir:
        p, q = x+dx, y+dy
        if 0 > p or 0 > q or n <= p or m <= q:
            continue
        if f == 0:
            if board[p][q] == '1':
                if visited[p][q][1] == float('inf'):
                    visited[p][q][1] = visited[x][y][0]+1
                    queue.append((p, q, 1))
            else:
                if visited[p][q][0] == float('inf'):
                    visited[p][q][0] = visited[x][y][0]+1
                    queue.append((p, q, 0))
        elif board[p][q] == '0' and visited[p][q][1] == float('inf'):
            visited[p][q][1] = visited[x][y][1]+1
            queue.append((p, q, 1))
else:
    print(-1)


