# https://www.acmicpc.net/problem/14226


from collections import deque

n = int(input())
queue = deque()
check = set()

queue.append([1, 0, 0])  # [화면, 클립보드, 시간]
check.add((1, 0))
while queue[0][0] != n:
    s, c, t = queue.popleft()

    for state in [(s, s), (s+c, c), (s-1, c)]:
        if state not in check:
            check.add(state)
            queue.append([*state, t+1])

print(queue[0][2])
