# https://www.acmicpc.net/problem/16930


from collections import deque

n, m, k = map(int, input().split())
board = [[*input()] for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
x1, y1, x2, y2 = map(lambda e: int(e)-1, input().split())

queue = deque()
queue.append((x1, y1))
visited[x1][y1] = 0

while queue:
    x, y = queue.popleft()
    if x == x2 and y == y2:
        break

    for dir in dirs:
        p, q = x, y
        for _ in range(k):
            p, q = p + dir[0], q + dir[1]
            if p < 0 or n <= p or q < 0 or m <= q or board[p][q] == '#':
                break
            if visited[p][q] == -1:
                visited[p][q] = visited[x][y] + 1
                queue.append((p, q))
            elif visited[x][y] + 1 > visited[p][q]:
                break

print(visited[x2][y2])