# https://programmers.co.kr/learn/courses/30/lessons/64061


def solution(board, moves):
    n = len(board)
    new_board = []
    answer = 0

    for j in range(n):
        new_board.append([])
        for i in range(n-1, -1, -1):
            if board[i][j] == 0:
                break
            new_board[-1].append(board[i][j])

    basket = []
    for move in moves:
        if basket and new_board[move-1] and basket[-1] == new_board[move-1][-1]:
            basket.pop()
            new_board[move-1].pop()
            answer += 2
        elif new_board[move-1]:
            basket.append(new_board[move-1][-1])
            new_board[move-1].pop()
    return answer


print(solution(eval(input()), eval(input())))
