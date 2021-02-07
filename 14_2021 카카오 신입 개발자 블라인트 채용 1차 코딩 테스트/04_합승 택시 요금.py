# https://programmers.co.kr/learn/courses/30/lessons/72413


import heapq


def solution (n, s, a, b, fares):
    answer = float('inf')
    graph = [[] for _ in range(n)]
    fares = [*map(lambda e: [e[0]-1, e[1]-1, e[2]], fares)]

    for v, u, cost in fares:
        graph[v].append((cost, u))
        graph[u].append((cost, v))

    def dijkstra(start):
        costs = [float('inf')] * n
        costs[start] = 0
        queue = [[costs[start], start]]

        while queue:
            cost_1, v = heapq.heappop(queue)
            if cost_1 < costs[v]:
                continue
            for cost_2, u in graph[v]:
                if cost_1 + cost_2 < costs[u]:
                    costs[u] = cost_1 + cost_2
                    heapq.heappush(queue, [costs[u], u])

        return costs

    costs_s = dijkstra(s - 1)
    costs_a = dijkstra(a - 1)
    costs_b = dijkstra(b - 1)

    for k in range(n):
        answer = min(answer, costs_s[k] + costs_a[k] + costs_b[k])

    return answer


print(solution(eval(input()), eval(input()), eval(input()), eval(input()), eval(input())))