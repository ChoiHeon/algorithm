# https://programmers.co.kr/learn/courses/30/lessons/49189


def solution(n, vertex):
    from collections import deque

    graph = [[] for _ in range(n)]
    distance = [0] + [float('inf')]*(n-1)
    queue = deque([(0, 0)])
    count = [0]*n
    longest = 0

    for edge in vertex:
        graph[edge[0]-1].append(edge[1]-1)
        graph[edge[1]-1].append(edge[0]-1)

    while queue:
        v, d = queue.popleft()
        count[d] += 1
        longest = max(longest, d)

        for u in graph[v]:
            if d+1 < distance[u]:
                distance[u] = d+1
                queue.append((u, d+1,))

    return count[longest]


print(solution(eval(input()), eval(input())))
