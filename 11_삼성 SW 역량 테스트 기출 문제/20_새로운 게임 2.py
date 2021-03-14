# https://www.acmicpc.net/problem/17837


n, k = map(int, input().split())
obj = [[] for _ in range(k)]
dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]
board = [[[] for _ in range(n)] for __ in range(n)]
grid_color = [[*map(int, input().split())] for _ in range(n)]

for i in range(k):
    r, c, d = map(int, input().split())
    obj[i] = [r-1, c-1, dir[d-1]]
    board[r-1][c-1].append(i)

turn = -1
boundary = 1000 * k
while turn <= boundary:
    turn += 1
    r, c, d = obj[turn % k]

    if r+d[0] < 0 or r+d[0] >= n or c+d[1] < 0 or c+d[1] >= n or grid_color[r+d[0]][c+d[1]] == 2:
        d = (-d[0], -d[1])
        obj[turn % k][2] = d
        if r+d[0] < 0 or r+d[0] >= n or c+d[1] < 0 or c+d[1] >= n or grid_color[r+d[0]][c+d[1]] == 2:
            continue

    i = board[r][c].index(turn % k)
    target = board[r][c][i:]
    board[r][c] =  board[r][c][:i]

    for j in target:
        obj[j][0] = r+d[0]
        obj[j][1] = c+d[1]

    if grid_color[r+d[0]][c+d[1]] == 1:
        target.reverse()
    board[r+d[0]][c+d[1]] += target

    if len(board[r+d[0]][c+d[1]]) >= 4:
        break

print(-1 if turn > boundary else (turn // k + 1))