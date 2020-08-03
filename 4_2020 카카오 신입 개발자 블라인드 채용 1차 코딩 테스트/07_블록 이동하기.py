# https://programmers.co.kr/learn/courses/30/lessons/60063


"""
* 풀이
    - 매번 로봇의 자표를 set 에 저장
    - 로봇이 이동하기 전, 이동하려는 좌표를 방문했는지 여부를 set 을 통해 확인
    - 로봇이 이동할 수 있는 경우를 잘 고려하는 것이 중요
"""


from collections import deque


def check(dq, log, p_x, p_y, q_x, q_y, new_time):
    if ((p_x, p_y), (q_x, q_y)) not in log:
        dq.append(((p_x, p_y), (q_x, q_y), new_time))
        log.add(((p_x, p_y), (q_x, q_y)))


def solution(board):
    n = len(board)
    log = set()
    log.add(((0, 0), (0, 1)))
    dq = deque([((0, 0), (0, 1), 0)])

    while True:
        a, b, time = dq.popleft()
        a_x, a_y, b_x, b_y, new_time = a[0], a[1], b[0], b[1], time+1
        shape = 1 if a[0] == b[0] else 0

        # Check 8 cases each type
        if shape:    # row
            if 0 < a_y and board[a_x][a_y-1] == 0:
                check(dq, log, a_x, a_y-1, b_x, b_y-1, new_time)    # move left
            if b_y < n-1 and board[b_x][b_y+1] == 0:
                if b_x == b_y+1 == n-1:
                    return new_time
                check(dq, log, a_x, a_y+1, b_x, b_y+1, new_time)    # move right
            if 0 < a_x and board[a_x-1][a_y] == board[b_x-1][b_y] == 0:
                check(dq, log, a_x-1, a_y, b_x-1, b_y, new_time)    # move up
                check(dq, log, b_x-1, b_y, b_x, b_y, new_time)      # turn up & right
                check(dq, log, a_x-1, a_y, a_x, a_y, new_time)      # turn up & left
            if a_x < n-1 and board[a_x+1][a_y] == board[b_x+1][b_y] == 0:
                if b_x+1 == b_y == n-1:
                    return new_time
                check(dq, log, a_x+1, a_y, b_x+1, b_y, new_time)    # move down
                check(dq, log, a_x, a_y, a_x+1, a_y, new_time)      # turn down & right
                check(dq, log, b_x, b_y, b_x+1, b_y, new_time)      # turn down & left
        else:       # column
            if 0 < a_x and board[a_x-1][a_y] == 0:
                check(dq, log, a_x-1, a_y, b_x-1, b_y, new_time)    # move up
            if b_x < n-1 and board[b_x+1][b_y] == 0:
                if b_x+1 == b_y == n-1:
                    return new_time
                check(dq, log, a_x+1, a_y, b_x+1, b_y, new_time)    # move down
            if 0 < a_y and board[a_x][a_y-1] == board[b_x][b_y-1] == 0:
                check(dq, log, a_x, a_y-1, b_x, b_y-1, new_time)    # move left
                check(dq, log, a_x, a_y-1, a_x, a_y, new_time)      # turn up & right
                check(dq, log, b_x, b_y-1, b_x, b_y, new_time)      # turn down & left
            if a_y < n-1 and board[a_x][a_y+1] == board[b_x][b_y+1] == 0:
                if b_x == b_y+1 == n-1:
                    return new_time
                check(dq, log, a_x, a_y+1, b_x, b_y+1, new_time)    # move right
                check(dq, log, a_x, a_y, a_x, a_y+1, new_time)      # turn up & left
                check(dq, log, b_x, b_y, b_x, b_y+1, new_time)      # turn down & right


input_data = input()
print(solution(eval(input_data)))