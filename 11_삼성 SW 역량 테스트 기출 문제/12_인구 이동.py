# https://www.acmicpc.net/problem/16234


import sys
read = sys.stdin.readline

n, l, r = map(int, read().split())
board = [[*map(int, read().split())] for _ in range(n)]

for answer in range(2001):
    visited = set()
    unions = []
    for i in range(n):
        for j in range(n):
            if (i, j) not in visited:
                union = set()
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    union.add((x, y,))
                    if (x-1, y) not in union and x > 0 and l <= abs(board[x][y]-board[x-1][y]) <= r:
                        stack.append((x-1, y,))
                    if (x+1, y) not in union and x+1 < n and  l <= abs(board[x][y]-board[x+1][y]) <= r:
                        stack.append((x+1, y,))
                    if (x, y-1) not in union and y > 0 and l <= abs(board[x][y]-board[x][y-1]) <= r:
                        stack.append((x, y-1,))
                    if (x, y+1) not in union and y+1 < n and l <= abs(board[x][y]-board[x][y+1]) <= r:
                        stack.append((x, y+1,))
                visited.update(union)
                if len(union) > 1:
                    unions.append(union)
    if not unions:
        break
    for union in unions:
        total = sum(map(lambda e: board[e[0]][e[1]], union))
        cnt = total // len(union)
        for nation in union:
            board[nation[0]][nation[1]] = cnt

print(answer)