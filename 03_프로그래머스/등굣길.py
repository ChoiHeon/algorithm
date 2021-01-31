# https://programmers.co.kr/learn/courses/30/lessons/42898?language=python3


def solution(m, n, puddles):
    board = [[0] * m for _ in range(n)]

    board[0][0] = 1
    for y, x in puddles:
        board[x - 1][y - 1] = -1

    for i in range(n):
        for j in range(m):
            if board[i][j] == -1:
                continue
            if i < n - 1 and board[i + 1][j] != -1:
                board[i + 1][j] += board[i][j]
            if j < m - 1 and board[i][j + 1] != -1:
                board[i][j + 1] += board[i][j]

    return board[n-1][m-1] % 1000000007


print(solution(eval(input()), eval(input()), eval(input())))