# https://programmers.co.kr/learn/courses/30/lessons/17679

import numpy


def solution(m, n, board):
    board = [[*line] for line in board]
    new_board = [[board[m-i-1][j] for i in range(m)] for j in range(n)]
    answer = 0

    is_updated = True
    while is_updated:
        is_updated = False
        del_targets = set()

        for i in range(n-1):
            for j in range(m-1):
                if new_board[i][j] == new_board[i][j+1] == new_board[i+1][j] == new_board[i+1][j+1] != 0:
                    del_targets.update({(i, j), (i, j+1), (i+1, j), (i+1, j+1)})
                    is_updated = True

        answer += len(del_targets)

        for i in range(n):
            for j in range(m):
                if (i, j, ) in del_targets:
                    new_board[i][j] = 0

        for i in range(n):
            del_cnt = 0
            for j in range(m):
                block = new_board[i].pop(0)
                if block != 0:
                    new_board[i].append(block)
                else:
                    del_cnt += 1
            new_board[i] += [0]*del_cnt

    return answer


print(solution(eval(input()), eval(input()), eval(input())))
