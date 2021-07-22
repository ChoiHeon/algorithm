# https://www.acmicpc.net/problem/16948


from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
dir = [(0, -2), (-2, -1), (-2, 1), (0, 2), (2, 1), (2, -1)]
visited = [[-1] * n for _ in range(n)]
queue = deque()

visited[r1][c1] = 0
queue.append((r1, c1))
while queue:
    r, c = queue.popleft()
    if r == r2 and c == c2:
        break

    for dir_r, dir_c in dir:
        p, q = r + dir_r, c + dir_c

        if p < 0 or n <= p or q < 0 or n <= q:
            continue
        if visited[p][q] != -1:
            continue

        visited[p][q] = visited[r][c] + 1
        queue.append((p, q))

print(visited[r2][c2])