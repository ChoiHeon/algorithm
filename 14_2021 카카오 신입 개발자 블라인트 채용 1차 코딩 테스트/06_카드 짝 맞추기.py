# https://programmers.co.kr/learn/courses/30/lessons/72415


"""
BFS를 이용해 가장 특정 좌표로 이동하는데 필요한 최소 이동 횟수를 탐색
탐색 종료 조건을 pop보다 push할 때 확인하는 것이 더 빠름
"""


def solution(board, r, c):
    from collections import deque, defaultdict
    from itertools import permutations

    def move_cursor(current: tuple, target: tuple):
        if current == target:
            return 0

        queue = deque()
        visited = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue.append((current, 0))
        visited.add(current)

        while queue:
            cursor, count = queue.popleft()

            for i, j in dirs:
                x, y = cursor[0] + i, cursor[1] + j
                if x < 0 or x > 3 or y < 0 or y > 3:
                    continue

                if (x, y) not in visited:
                    if (x, y) == target:
                        return count + 1
                    queue.append(((x, y), count + 1))
                    visited.add((x, y))

                while 0 <= x < 4 and 0 <= y < 4:
                    if board[x][y]:
                        if (x, y) not in visited:
                            if (x, y) == target:
                                return count + 1
                            queue.append(((x, y), count + 1))
                            visited.add((x, y))
                        break
                    x, y = x + i, y + j
                else:
                    x, y = x - i, y - j
                    if (x, y) not in visited:
                        if (x, y) == target:
                            return count + 1
                        queue.append(((x, y), count + 1))
                        visited.add((x, y))

    num_by_pos = dict()
    pos_by_num = defaultdict(list)

    for i in range(4):
        for j in range(4):
            if board[i][j]:
                num_by_pos[(i, j)] = board[i][j]
                pos_by_num[board[i][j]].append((i, j))

    n = len(pos_by_num.keys())
    start = (r, c)
    answer = float('inf')
    cases = permutations(pos_by_num.values())
    choices = [*map(lambda x: [*map(int, bin(x)[2:].zfill(n))], range(2 ** n))]
    choices = [*map(lambda x: [*map(lambda y: (0, 1) if y else (1, 0), x)], choices)]

    for case in cases:
        for choice in choices:
            order = []
            pos_a = start
            count = 0
            for i in range(n):
                order.append(case[i][choice[i][0]])
                order.append(case[i][choice[i][1]])
            for i in range(0, n * 2, 2):
                pos_b, pos_c = order[i], order[i + 1]
                count += move_cursor(pos_a, pos_b)
                count += move_cursor(pos_b, pos_c)
                board[pos_b[0]][pos_b[1]] = board[pos_c[0]][pos_c[1]] = 0
                pos_a = pos_c
            answer = min(answer, count)
            for pos in num_by_pos.keys():
                board[pos[0]][pos[1]] = num_by_pos[pos]

    return answer + (n * 2)


print(solution(eval(input()), eval(input()), eval(input())))