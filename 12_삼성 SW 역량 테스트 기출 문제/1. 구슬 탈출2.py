# https://www.acmicpc.net/problem/13460


def solution():
    m, n = map(int, input().split())
    board = [[-1]*n for _ in range(m)]
    r_pos = None
    b_pos = None
    h_pos = None

    for i in range(m):
        row = [*input()]
        for j in range(n):
            board[i][j] = row[j]
            if r_pos == None and row[j] == 'R':
                r_pos = (i, j)
            elif b_pos == None and row[j] == 'B':
                b_pos = (i, j)
            elif h_pos == None and row[j] == 'O':
                h_pos = (i, j)

    log = {(r_pos, b_pos)}
    bfs = [(r_pos, b_pos)]
    for i in range(1, 11):
        for _ in range(len(bfs)):
            r, b = bfs.pop(0)
            for p, q in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                next_r, next_b = r, b
                goal_in_r = goal_in_b = False
                while True:
                    prev_r, prev_b = next_r, next_b
                    if not goal_in_r and board[next_r[0]+p][next_r[1]+q] != '#':
                        next_r = (next_r[0]+p, next_r[1]+q)
                    if not goal_in_b and board[next_b[0]+p][next_b[1]+q] != '#':
                        next_b = (next_b[0]+p, next_b[1]+q)
                    if prev_r == next_r and prev_b == next_b:
                        break
                    if next_r == next_b:
                        next_r, next_b = prev_r, prev_b
                        break
                    if next_r == h_pos:
                        goal_in_r = True
                        next_r = (-1, -1)
                    if next_b == h_pos:
                        goal_in_b = True
                        next_b = (-1, -1)
                if not goal_in_b:
                    if goal_in_r:
                        return i
                    if (next_r, next_b) not in log:
                        bfs.append((next_r, next_b))
                        log.add((next_r, next_b))
    return -1


print(solution())

