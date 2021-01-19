# https://www.acmicpc.net/problem/17144


r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
dust = []
upper, lower = [], []
around = [[[0] for _ in range(c)] for _ in range(r)]

# dust & upper & lower
for i in range(r):
    for j in range(c):
        if board[i][j] == -1:
            if not upper:   upper.append((i, j))
            else:           lower.append((i, j))
        else:
            dust.append((i, j))

# upper
pos = upper.pop()
for i in range(1, c):               upper.append((pos[0], i))
for i in range(pos[0]-1, -1, -1):   upper.append((i, c-1))
for i in range(c-2, -1, -1):        upper.append((0, i))
for i in range(1, pos[0]):          upper.append((i, 0))

# lower
pos = lower.pop()
for i in range(1, c):               lower.append((pos[0], i))
for i in range(pos[0]+1, r):        lower.append((i, c-1))
for i in range(c-2, -1, -1):        lower.append((r-1, i))
for i in range(r-2, pos[0], -1):    lower.append((i, 0))

# around
for i, j in dust:
    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if -1 < i+x < r and -1 < j+y < c and board[i+x][j+y] != -1:
            around[i][j][0] += 1
            around[i][j].append((i+x, j+y))

for _ in range(t):
    temp = [[0]*c for _ in range(r)]

    for i, j in dust:
        cnt, e = around[i][j][0], board[i][j] // 5
        board[i][j] -= (e * cnt)
        for p, q in around[i][j][1:]:
            temp[p][q] += e

    for i, j in dust:
        board[i][j] += temp[i][j]

    prev = 0
    for x, y in upper:
        prev, board[x][y] = board[x][y], prev

    prev = 0
    for x, y in lower:
        prev, board[x][y] = board[x][y], prev

answer = 0
for i, j in dust:
    answer += board[i][j]

print(answer)













