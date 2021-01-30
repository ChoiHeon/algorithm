# https://programmers.co.kr/learn/courses/30/lessons/43162


from collections import defaultdict


def solution(n, computers):
    visited = [0] * n
    edges = defaultdict(list)
    answer = 0

    for i in range(n):
        for j in range(n):
            if i == j or computers[i][j] == 0:
                continue
            edges[i].append(j)



    for i in range(n):
        if visited[i] == 1:
            continue

        stack = [i]
        while stack:
            p = stack.pop()
            for q in edges[p]:
                if visited[q] == 1:
                    continue
                visited[q] = 1
                stack.append(q)
        answer += 1

    return answer



