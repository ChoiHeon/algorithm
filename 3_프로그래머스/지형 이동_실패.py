# https://programmers.co.kr/learn/courses/30/lessons/62050

"""
* 2차원 배열을 이용한 유니온 파인드를 통해 그래프로 전환
    - 크루스칼 알고리즘 사용
"""


import sys
sys.setrecursionlimit(10**6)


def solution(land, height):
    n = len(land)
    parents = [[n*i+j for j in range(n)] for i in range(n)]

    def find(x):
        if x == parents[x//n][x%n]:
            return x
        parents[x//n][x%n] = find(parents[x//n][x%n])
        return parents[x//n][x%n]

    def union(x, y):
        x, y = find(x), find(y)
        if x > y:
            parents[x//n][x%n] = y
        else:
            parents[y//n][y%n] = x

    # 유니온 파인드를 이용한 그룹 생성
    for i in range(n):
        for j in range(n):
            if i < n-1 and abs(land[i][j]-land[i+1][j]) <= height:
                union(i*n+j, (i+1)*n+j)
            if j < n-1 and abs(land[i][j]-land[i][j+1]) <= height:
                union(i*n+j, i*n+(j+1))

    # 인접한 그룹간 최소거리 탐색
    dist = {}
    for i in range(n):
        for j in range(n):
            if i < n-1 and find(i*n+j) != find((i+1)*n+j):
                pair = (*sorted([find(i*n+j), find((i+1)*n+j)]),)
                if pair not in dist:
                    dist[pair] = abs(land[i][j]-land[i+1][j])
                else:
                    dist[pair] = min(dist[pair], abs(land[i][j]-land[i+1][j]))
            if j < n-1 and find(i*n+j) != find(i*n+(j+1)):
                pair = (*sorted([find(i*n+j), find(i*n+(j+1))]),)
                if pair not in dist:
                    dist[pair] = abs(land[i][j]-land[i][j+1])
                else:
                    dist[pair] = min(dist[pair], abs(land[i][j]-land[i][j+1]))

    # 크루스칼 알고리즘을 이용한 MST 탐색
    dist = {dist[k]:k for k in dist}
    parents2 = {}
    answer = 0

    def find2(x):
        if x == parents2[x]:
            return x
        parents2[x] = find2(parents2[x])
        return parents2[x]

    def union2(x, y):
        x, y = find2(x), find2(y)
        if x > y:
            parents2[x] = y
        else:
            parents2[y] = x

    for i in range(n):
        for j in range(n):
            if find(parents[i][j]) not in parents2:
                parents2[find(parents[i][j])] = find(parents[i][j])

    for d in sorted([*dist.keys()]):
        if find2(dist[d][0]) != find2(dist[d][1]):
            union2(dist[d][0], dist[d][1])
            answer += d
        if len(set(parents2.values())) == 1:
            return answer

    print(parents2)

    return answer


print(solution(eval(input()), eval(input())))
