# https://programmers.co.kr/learn/courses/30/lessons/68937




from collections import deque


def solution(n, edges):
    graph = {i:[] for i in range(n)}


    def bfs(s):
        queue = deque([s])
        dists = [-1] * n
        dists[s] = 0
        while queue:
            v = queue.popleft()
            for u in graph[v]:
                if dists[u] == -1:
                    dists[u] = dists[v] + 1
                    queue.append(u)
        return dists


    for edge in edges:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)

    dists_tmp = bfs(0)
    start = dists_tmp.index(max(dists_tmp))

    dists_start = bfs(start)
    end = dists_start.index(max(dists_start))
    dists_end = bfs(end)

    answer = 0
    for i in range(n):
        if i == start or i == end:
            continue
        answer = max(answer, max(dists_start[i], dists_end[i]))
    return answer



print(solution(eval(input()), eval(input())))
