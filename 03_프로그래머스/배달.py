# https://programmers.co.kr/learn/courses/30/lessons/12978


import heapq


def solution(n, road, k):
    graph = [[float('inf')]*n for _ in range(n)]

    for v, u, c in road:
        graph[v-1][u-1] = min(graph[v-1][u-1], c)
        graph[u-1][v-1] = min(graph[u-1][v-1], c)

    costs = [float('inf')] * n
    costs[0] = 0
    queue = [[costs[0], 0]]

    while queue:
        c, v = heapq.heappop(queue)
        if c < costs[v]:
            continue
        for u in range(n):
            if graph[v][u] == float('inf'):
                continue
            if c + graph[v][u] < costs[u]:
                costs[u] = c + graph[v][u]
                heapq.heappush(queue, [costs[u], u])

    return len([*filter(lambda e: e <= k, queue)])


# test
print(solution(eval(input()), eval(input()), eval(input())))