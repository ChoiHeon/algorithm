# coding=utf-8
# https://programmers.co.kr/learn/courses/30/lessons/42894


def find(n, board):
    ret = set()
    for j in range(n):
        for i in range(n):
            if board[i][j]:
                break
            ret.add((i, j, ))
    return ret


def solution(board):
    answer = 0
    n = len(board)
    block_idx = set()       # 블록들의 번호
    block_1 = dict()        # 블록들의 좌표
    block_2 = dict()        # 블록들의 필요한 자표

    # block_1
    for i in range(n):
        for j in range(n):
            if board[i][j]: # 블록이 있을 경우
                if board[i][j] not in block_1.keys():
                    block_1[board[i][j]] = []
                    block_2[board[i][j]] = set()
                block_1[board[i][j]].append((i, j, ))
                block_idx.add(board[i][j])

    # block_2
    for i in block_idx:
        row = set(map(lambda e: e[0], block_1[i]))
        col = set(map(lambda e: e[1], block_1[i]))
        for x in row:
            for y in col:
                if board[x][y] != i:
                    block_2[i].add((x, y, ))

    flag = True
    while flag:
        flag = False
        black_block = find(n, board)

        for i in block_idx.copy():
            if block_2[i] <= black_block:       # 블랙 블록들 중 필요한 블록이 있을 경우
                block_idx.remove(i)
                answer += 1
                flag = True
                for x, y in block_1[i]:
                    board[x][y] = 0

    return answer


input_data = input()
print(solution(eval(input_data)))