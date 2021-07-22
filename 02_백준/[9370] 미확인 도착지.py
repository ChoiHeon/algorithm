# https://www.acmicpc.net/problem/15956


"""
다익스트라 알고리즘을 활용한 문제
복수의 정점에 대한 다익스트라 알고리즘을 활용하여
특정 경로를 지나는 최단거리를 구할 수 있다
"""


import sys, heapq
input = sys.stdin.readline

for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(lambda e: int(e)-1, input().split())
    graph = [[] for _ in range(n)]
    g_to_h = 0      # h_to_g

    for _ in range(m):
        a, b, d = map(int, input().split())
        a, b = a-1, b-1
        graph[a].append([b, d])
        graph[b].append([a, d])
        if {a, b} == {g, h}:
            g_to_h = d


    def dijkstra(start):
        dists = [float('inf')] * n
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


    dist_from_s = dijkstra(s)   # distances from s
    dist_from_g = dijkstra(g)   # distances from g
    dist_from_h = dijkstra(h)   # distances from h

    s_to_g = dist_from_s[g]        # s -> g
    s_to_h = dist_from_s[h]        # s -> h

    answer = []
    for _ in range(t):
        x = int(input())-1
        s_to_x = dist_from_s[x]
        h_to_x = dist_from_h[x]
        g_to_x = dist_from_g[x]

        # s->x == min(s->g->h->x , s->h->g->x)
        if s_to_x != float('inf') and s_to_x == (min(s_to_g + h_to_x, s_to_h + g_to_x) + g_to_h):
            answer.append(x+1)

    print(" ".join(map(str, sorted(answer))))
