# https://www.acmicpc.net/problem/17825


from collections import deque


class Node:
    def __init__(self, score):
        self.score = score
        self.red = None
        self.blue = None

    def get_next(self, is_start):
        if self.score == 42:
            return self
        if is_start and self.blue != None:
            return self.blue
        return self.red


def find(node, target):
    if node.score == target:
        return node
    return find(node.red, target)


def move(node, count):
    dest = node.get_next(True)
    for i in range(count-1):
        dest = dest.get_next(False)
    return dest


def create_board():
    start = Node(0)
    finish = Node(42)
    inter = Node(25)

    def link(node_from, node_to, scores):
        cursor = node_from
        for score in scores:
            node = Node(score)
            cursor.red = node
            cursor = node
        cursor.red = node_to

    link(start, finish, range(2, 42, 2))

    cursor = find(start, 10)
    cursor.blue = Node(13)
    link(cursor.blue, inter, [16, 19])

    cursor = find(start, 20)
    cursor.blue = Node(22)
    link(cursor.blue, inter, [24])

    cursor = find(start, 30)
    cursor.blue = Node(28)
    link(cursor.blue, inter, [27, 26])

    link(inter, find(start, 40), [30, 35])

    return start


dices = [*map(int, input().split())]
start = create_board()
dq = deque()
answer = -1

state = [start, start, start, start, 0, 0]  # 돌 1~4, 점수 합, 턴 수
dq.append(state)

while dq:
    state = dq.popleft()
    stones = state[:4]
    total = state[4]
    turn = state[5]

    if turn == 10:
        answer = max(answer, total)
        continue

    for i in range(4):
        stone = stones[i]
        next = move(stone, dices[turn])

        if next.score != 42 and next in stones:  # 도착 지점이 아니라면 중복된 위치를 허용하지 않음
            continue

        new_state = state.copy()
        new_state[i] = next
        new_state[4] = total + (0 if next.score == 42 else next.score)
        new_state[5] += 1

        dq.append(new_state)

print(answer)



