# https://www.acmicpc.net/problem/1197


"""
* 크루스칼 알고리즘을 이용한 MST(최소 스패닝 트리) 탐색
* 크루스칼 알고리즘
    - 그리디 알고리즘과 유니온 파인드를 활용
    - 가중치가 낮은 간선부터 차례로 확인
    - 유니온 파인드를 통해 간선이 연결중인 노드들이 사이클을 생성하는지 확인
"""


import sys
input = sys.stdin.readline

V, E = map(int, input().split())
parents = [*range(V+1)]
edges = []

for _ in range(E):
    edges.append(list(map(int, input().split())))
edges.sort(key=lambda e: e[2])


def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)
    parents[x] = y


answer = 0
for edge in edges:
    v, u, w = edge
    if find(v) != find(u):
        answer += w
        union(v, u)

print(answer)





