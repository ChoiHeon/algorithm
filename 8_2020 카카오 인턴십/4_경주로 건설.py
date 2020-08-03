# https://programmers.co.kr/learn/courses/30/lessons/67259


def solution(board):
    n = len(board)
    cost_board = [[float('inf')]*n for _ in range(n)]
    stack = [((0,0), (-1, -1), 0)]    # 현재좌표, 이전좌표, 비용

    while stack:
        current_pos, prev_pos, cost = stack.pop()
        if current_pos == (n - 1, n - 1):
            continue
        for dir_x, dir_y in zip([-1, 1, 0, 0], [0, 0, -1, 1]):  # 상하좌우

            next_pos = (current_pos[0] + dir_x, current_pos[1] + dir_y)
            if -1 < next_pos[0] < n and -1 < next_pos[1] < n and board[next_pos[0]][next_pos[1]] == 0:
                next_cost = 100 if abs(prev_pos[0] - next_pos[0]) == 2 or abs(prev_pos[1] - next_pos[1]) == 2 else 600
                next_cost += cost
                if next_cost <= cost_board[next_pos[0]][next_pos[1]]:
                    cost_board[next_pos[0]][next_pos[1]] = next_cost
                    stack.append((next_pos, current_pos, next_cost))

    return cost_board[n-1][n-1]



print(solution(eval(input())))
