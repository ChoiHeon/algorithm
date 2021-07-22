# https://www.acmicpc.net/problem/9328


from collections import defaultdict


def solution():
    h, w = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    key = {*input()}
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    visited = [[False]*w for _ in range(h)]
    staying = defaultdict(set)
    answer = 0
    stack = []

    for i in range(h):
        if board[i][0] != '*':
            stack.append([i, 0])
        if board[i][w-1] != '*':
            stack.append([i, w-1])
    for j in range(1, w-1):
        if board[0][j] != '*':
            stack.append([0, j])
        if board[h-1][j] != '*':
            stack.append([h-1, j])

    while stack:
        x, y = stack.pop()

        if visited[x][y]:
            continue
        visited[x][y] = True
        if board[x][y] == '$':  # 문서
            answer += 1
            board[x][y] = '.'
        elif board[x][y].islower():  # 열쇠
            key.add(board[x][y])
            for rx, ry in staying[board[x][y]]:
                stack.append([rx, ry])
                visited[rx][ry] = False
            staying[board[x][y]].clear()
            board[x][y] = '.'
        elif board[x][y].isupper():  # 문
            if board[x][y].lower() not in key:  # 열쇠가 없을 경우
                staying[board[x][y].lower()].add((x, y))
                continue
            else:  # 열쇠가 있을 경우
                board[x][y] = '.'

        for dx, dy in dir:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] != '*':
                stack.append([nx, ny])

    return answer


for _ in range(int(input())):
    print(solution())