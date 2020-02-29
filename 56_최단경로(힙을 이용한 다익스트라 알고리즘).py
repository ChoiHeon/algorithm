# https://www.acmicpc.net/problem/1753


"""
방향과 가중치가 주어진 그래프에 대하여
특정 정점에 대한 나머지 정점들의 최단거리를 구하는 문제
--> 다익스트라 알고리즘

다익스트라 알고리즘
1. 시작 정점(v)에서 바로 연결된 노드들(u)을 선정
2. 연결된 노드들에 대한 최단거리를 갱신 --> d(u) = min(d(u), d(v) + w(v, u))
3. v를 제외한 노드들 중 최단거리가 가장 짧은 노드를 선정
4. 2와 3을 반복
"""

import sys, heapq
input = sys.stdin.readline
INF = float("inf")
v_cnt, e_cnt = map(int, input().split())
graph = [[] * v_cnt for _ in range(v_cnt)]
distance = [INF] * v_cnt
heap = []

v = int(input())-1
distance[v] = 0
heap.append((distance[v], v,))

for _ in range(e_cnt):
    p, q, e = map(int, input().split())
    graph[p-1].append((q-1, e),)

while heap:
    w, v = heapq.heappop(heap)
    if distance[v] < w:
        continue

    for next_v, next_w in graph[v]:
        next_w += w
        if next_w < distance[next_v]:
            heapq.heappush(heap, (next_w, next_v))
            distance[next_v] = next_w

for ans in distance:
    print(ans) if ans != INF else print("INF")

