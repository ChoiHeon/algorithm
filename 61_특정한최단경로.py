# https://www.acmicpc.net/problem/15956


"""
다익스트라 알고리즘을 활용한 문제
어느 한 정점에서 복수의 정점에 대해 최단거리를 구해야 하고
간선에 음의 가중치가 없으므로 다익스트라 알고리즘을 사용
반드시 거쳐야 하는 정점 P, Q에 대해 다익스트라 알고리즘을 실행하여
최단거리의 합 중 최소값을 찾는다
"""


import sys, heapq
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N)]

# 출발 지점을 0, 도착 지점을 N-1이라 가정
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a-1].append([b-1, c])
    graph[b-1].append([a-1, c])

P, Q = map(lambda x: int(x)-1, input().split())


def dijkstra(start):
    dists = [float('inf')] * N
    heap = []
    dists[start] = 0
    heap.append([0, start])

    while heap:
        dist, vertex = heapq.heappop(heap)
        if dist > dists[vertex]:
            continue

        for next_vertex, next_cost in graph[vertex]:
            if dists[next_vertex] > dist + next_cost:
                dists[next_vertex] = dist + next_cost
                heapq.heappush(heap, [dists[next_vertex], next_vertex])

    return dists


dist_from_0 = dijkstra(0)   # distances from 0
dist_from_P = dijkstra(P)   # distances from P
dist_from_Q = dijkstra(Q)   # distances from Q

a = dist_from_0[P]        # 0 -> P
b = dist_from_0[Q]        # 0 -> Q
c = dist_from_P[Q]        # p -> Q ( == Q -> P)
d = dist_from_P[-1]       # P -> (N-1)
e = dist_from_Q[-1]       # Q -> (N-1)

answer = min(a+e, b+d) + c
print(answer) if answer != float('inf') else print(-1)

