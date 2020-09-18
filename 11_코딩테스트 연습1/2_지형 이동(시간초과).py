# https://programmers.co.kr/learn/courses/30/lessons/62050

"""
* DFS와 set을 이용하여 그래프로 전환
    - 크루스칼 알고리즘을 통해 그래프의 최단거리 순회 탐색
    - 시간초과 발생

* 2차원 배열을 이용한 유니온 파인드를 통해 그래프로 전환
    - 크루스칼 알고리즘 사용
"""


def solution(land, height):
    n = len(land)
    h_ladders = [[0] * (n-1) for _ in range(n)]
    v_ladders = [[0] * n for _ in range(n-1)]
    for i in range(n):
        for j in range(n):
            if j < n-1:   h_ladders[i][j] = abs(land[i][j+1]-land[i][j]) if abs(land[i][j+1]-land[i][j]) > height else 0
            if i < n-1:   v_ladders[i][j] = abs(land[i+1][j]-land[i][j]) if abs(land[i+1][j]-land[i][j]) > height else 0

    nodes = [];     visited = set()
    for i in range(n):
        for j in range(n):
            if (i, j) not in visited:
                node = {(i, j)};    stack = [(i, j)]
                while stack:
                    p, q = stack.pop()
                    if q < n-1 and not h_ladders[p][q] and (p, q+1) not in node:
                        node.add((p, q+1));     stack.append((p, q+1))
                    if p < n-1 and not v_ladders[p][q] and (p+1, q) not in node:
                        node.add((p+1, q));     stack.append((p+1, q))
                    if 0 < q and not h_ladders[p][q-1] and (p, q-1) not in node:
                        node.add((p, q-1));     stack.append((p, q-1))
                    if 0 < p and not v_ladders[p-1][q] and (p-1, q) not in node:
                        node.add((p-1, q));     stack.append((p-1, q))
                nodes.append(node);     visited.update(node)

    m = len(nodes)
    edges = []
    for i in range(m-1):
        for j in range(i+1, m):
            cost = float('inf')
            for i_x, i_y in nodes[i]:
                for j_x, j_y in nodes[j]:
                    k = (i_x-j_x, i_y-j_y)
                    if k == (1, 0):     cost = min(cost, v_ladders[j_x][j_y])
                    elif k == (-1, 0):  cost = min(cost, v_ladders[i_x][i_y])
                    elif k == (0, 1):   cost = min(cost, h_ladders[j_x][j_y])
                    elif k == (0, -1):  cost = min(cost, h_ladders[i_x][i_y])
            edges.append((cost, i, j))
    edges.sort(key=lambda e: e[0])

    parents = [*range(m)]
    def find(x):
        if x == parents[x]:  return x
        parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        x, y = find(x), find(y)
        parents[x] = y

    answer = 0
    for edge in edges:
        cost, v, u = edge
        if find(v) != find(u):
            answer += cost
            union(v, u)
    return answer


print(solution( eval(input()), eval(input())))
