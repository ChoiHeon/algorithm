# https://programmers.co.kr/learn/courses/30/lessons/1844


from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    queue = deque([((0, 0), 1)])
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[float('inf')]*m for _ in range(n)]

    while queue:
        pos, dist = queue.popleft()
        for dir in dirs:
            next = (pos[0]+dir[0], pos[1]+dir[1])
            if 0 > next[0] or n-1 < next[0] or 0 > next[1] or m-1 < next[1] or maps[next[0]][next[1]] == 0:
                continue
            if dist+1 < visited[next[0]][next[1]]:
                visited[next[0]][next[1]] = dist+1
                if next != (n-1, m-1):
                    queue.append((next, dist+1, ))

    return visited[n-1][m-1] if visited[n-1][m-1] != float('inf') else -1



print(solution(eval(input())))
