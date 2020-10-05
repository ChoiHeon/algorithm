# https://www.acmicpc.net/workbook/view/1152
# https://www.acmicpc.net/problem/14502


from itertools import combinations

n, m = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(n)]

empty = []
virus = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            empty.append((i, j,))
        elif board[i][j] == 2:
            virus.append((i, j,))

cnt = len(empty)
answer = float('-inf')

for walls in combinations(empty, 3):
    for wall in walls:  board[wall[0]][wall[1]] = 1

    stack = virus.copy()
    area = set(virus)
    ret = cnt-3

    while stack:
        y, x = stack.pop()
        for q, p in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 > x+p or x+p > m-1 or 0 > y+q or y+q > n-1:
                continue
            if board[y+q][x+p] == 0 and (y+q, x+p,) not in area:
                area.add((y+q, x+p,))
                stack.append((y+q, x+p,))
                ret -= 1

    answer = max(answer, ret)

    for wall in walls:  board[wall[0]][wall[1]] = 0

print(answer)


