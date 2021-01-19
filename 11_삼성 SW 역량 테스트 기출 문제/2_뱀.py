# https://www.acmicpc.net/problem/12100


from collections import deque


def solution():
    n = int(input())
    board = [[0]*n for _ in range(n)]

    k = int(input())
    for _ in range(k):
        pos = [*map(int, input().split())]
        board[pos[0]-1][pos[1]-1] = 1

    move = [''] * 10000
    for _ in range(int(input())):
        info = input().split()
        move[int(info[0])] = info[1]

    board[0][0] = 2
    snake = deque([[0, 0]])
    dir_info = deque([(1,0), (0,-1), (-1,0)])
    dir = (0, 1)
    for i in range(10000):
        if move[i] == 'L':
            dir_info.appendleft(dir)
            dir = dir_info.pop()
        elif move[i] == 'D':
            dir_info.append(dir)
            dir = dir_info.popleft()

        next = [snake[0][0] + dir[0], snake[0][1] + dir[1]]
        if next[0] < 0 or next[0] > n-1 or next[1] < 0 or next[1] > n-1:
            return i+1
        if board[next[0]][next[1]] == 0:
            board[next[0]][next[1]] = 2
            snake.appendleft(next)
            board[snake[-1][0]][snake[-1][1]] = 0
            snake.pop()
        elif board[next[0]][next[1]] == 1:
            board[next[0]][next[1]] = 2
            snake.appendleft(next)
        elif board[next[0]][next[1]] == 2:
            return i+1


print(solution())

