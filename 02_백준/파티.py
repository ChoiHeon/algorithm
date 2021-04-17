# https://www.acmicpc.net/problem/1238

"""
* 문제 설명
    단방향 그래프에서 특정 정점 X에 대한 최단거리를 구하는 문제입니다.
    정점 X에서 시작애 모든 정점까지의 최단거리와 각 정점에서 정점 X까지의 거리를 구한 뒤
    X를 제외한 모든 정점 V에 대해 V에서 X, X에서 V까지 최단 거리의 합 중 가장 큰 값을 반환해야 합니다.

* 해결 방법
    1) 모든 정점에 대해 다익스트라 알고리즘을 실행합니다.
        - 시간복잡도가 O(N^2logN) 입니다.
    2) 그래프를 생성할 때, 주어진 방향과 반대되는 간선을 가진 그래프를 하나 더 생성합니다.
        - 주어진 방향의 그래프에서 X에 대한 다익스트라 알고리즘을 실행하면, X에서 각 정점까지의 최단 거리를 구할 수 있습니다.
        - 반대 방향의 그래프에서 X에 대한 다익스트라 알고리즘을 실행하면, 각 정점에서 X까지의 최단 거리를 구할 수 있습니다.
        - 즉, 다익스트라 알고리즘을 2번만 실행합니다.
"""

import heapq

N, M, X = map(int, input().split())
graph = [[[] for _ in range(N + 1)] for __ in range(2)]
dist = [[float('inf')] * (N + 1) for _ in range(2)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[0][a].append((b, c))
    graph[1][b].append((a, c))

for i in range(2):
    dist[i][X] = 0
    heap = [(0, X)]
    while heap:
        c1, v1 = heapq.heappop(heap)
        if c1 != dist[i][v1]:
            continue
        for v2, c2 in graph[i][v1]:
            if c1 + c2 < dist[i][v2]:
                dist[i][v2] = c1 + c2
                heapq.heappush(heap, (dist[i][v2], v2))

answer = max([a + b for a, b, in zip(dist[0][1:], dist[1][1:])])
print(answer)


'''
# 처음에 풀었던 코드
import heapq

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
dist = [[float('inf')]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

for i in range(1, N+1):
    dist[i][i] = 0
    heap = [(0, i)]
    while heap:
        c1, v1 = heapq.heappop(heap)
        if c1 != dist[i][v1]:
            continue
        for v2, c2 in graph[v1]:
            if c1 + c2 < dist[i][v2]:
                dist[i][v2] = c1 + c2
                heapq.heappush(heap, (dist[i][v2], v2))

answer = max([dist[i][X] + dist[X][i] for i in range(1, N+1) if i != X])
print(answer)
'''