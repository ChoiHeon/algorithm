# https://programmers.co.kr/learn/courses/30/lessons/77485


def solution(row, col, query):
    board = [[i*col+j+1 for j in range(col)] for i in range(row)]
    answer = []

    for q in query:
        a, b, c, d = map(lambda e: e-1, q)
        v = board[a][b]
        p, q = board[a][b], -1
        for j in range(b+1, d+1):  # right
            v = min(v, board[a][j])
            board[a][j], q = p, board[a][j]
            p, q = q, p
        for i in range(a+1, c+1):  # down
            v = min(v, board[i][d])
            board[i][d], q = p, board[i][d]
            p, q = q, p
        for j in range(d-1, b-1, -1):  # left
            v = min(v, board[c][j])
            board[c][j], q = p, board[c][j]
            p, q = q, p
        for i in range(c-1, a-1, -1):  # up
            v = min(v, board[i][b])
            board[i][b], q = p, board[i][b]
            p, q = q, p
        answer.append(v)

    return answer


# test
print(solution(eval(input()), eval(input()), eval(input())))