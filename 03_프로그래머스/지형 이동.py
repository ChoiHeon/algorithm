# https://programmers.co.kr/learn/courses/30/lessons/62050


from collections import deque
import sys
sys.setrecursionlimit(10**6)


def solution(land, height):
    n = len(land)
    visited = [[False]*n for _ in range(n)]
    groups = [[-1]*n for _ in range(n)]

    def bfs(i, j, num):
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([(i, j)])
        visited[i][j] = True
        while queue:
            x, y = queue.popleft()
            groups[x][y] = num
            for dx, dy in dir:
                if 0 <= x+dx < n and 0 <= y+dy < n and not visited[x+dx][y+dy] \
                        and abs(land[x][y]-land[x+dx][y+dy]) <= height:
                    visited[x+dx][y+dy] = True
                    queue.append((x+dx, y+dy,))

    # BFS를 이용한 그룹화
    group_num = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, group_num)
                group_num += 1

    # 인접한 그룹간 최소거리 탐색
    dist = {}
    for i in range(n):
        for j in range(n):
            if i < n-1 and groups[i][j] != groups[i+1][j]:
                pair = (*sorted([groups[i][j], groups[i+1][j]]), )
                if pair not in dist:
                    dist[pair] = abs(land[i][j]-land[i+1][j])
                else:
                    dist[pair] = min(dist[pair], abs(land[i][j]-land[i+1][j]))
            if j < n-1 and groups[i][j] != groups[i][j+1]:
                pair = (*sorted([groups[i][j], groups[i][j+1]]), )
                if pair not in dist:
                    dist[pair] = abs(land[i][j]-land[i][j+1])
                else:
                    dist[pair] = min(dist[pair], abs(land[i][j]-land[i][j+1]))

    parents = [*range(group_num)]
    dist = sorted(dist.items(), key=lambda e: e[1])
    answer = 0

    def find(x):
        if x == parents[x]:
            return x
        parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        x, y = find(x), find(y)
        if x > y:
            parents[x] = y
        else:
            parents[y] = x

    # 크루스칼 알고리즘을 이용해 MST 생성
    for info in dist:
        v, u = info[0]
        d = info[1]
        if find(v) != find(u):
            union(v, u)
            answer += d

    return answer












print(solution(eval(input()), eval(input())))
