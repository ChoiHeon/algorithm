# https://www.acmicpc.net/problem/4195


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

import sys
input = sys.stdin.readline

v_cnt, e_cnt = map(int, input().split())
adj = [[-1] * (v_cnt+1) for _ in range(v_cnt+1)]
link = [[] for _ in range(v_cnt+1)]
distance = [float("inf")] * (v_cnt+1)
is_visited = [False] * (v_cnt+1)

v = int(input())
distance[v] = 0


for _ in range(e_cnt):
    a, b, d = map(int, input().split())
    adj[a][b] = d
    link[a].append(b)

for _ in range(v_cnt):
    is_visited[v] = True

    for u in link[v]:
        distance[u] = min(distance[u], distance[v] + adj[v][u])

    min_dis = float("inf")

    for i in range(1, v_cnt+1):
        if not is_visited[i] and min_dis > distance[i]:
            v = i

for answer in distance[1:]:
    print(answer) if answer != float("inf") else print("INF")



