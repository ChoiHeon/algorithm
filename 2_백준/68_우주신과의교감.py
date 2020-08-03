# https://www.acmicpc.net/problem/1774


"""
* 크루스칼 알고리즘을 이용한 MST(최소 스패닝 트리) 탐색
* 크루스칼 알고리즘
    - 그리디 알고리즘과 유니온 파인드를 활용
    - 가중치가 낮은 간선부터 차례로 확인
    - 유니온 파인드를 통해 간선이 연결중인 노드들이 사이클을 생성하는지 확인
"""


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parents = [*range(N)]
pos = [] * N
dist = []

for _ in range(N):
    pos.append(list(map(int, input().split())))

for i in range(N):
    for j in range(i, N):
        d = abs(pos[i][0]-pos[j][0])**2 + abs(pos[i][1]-pos[j][1])**2
        dist.append([i, j, d])
dist.sort(key=lambda e: e[2])


def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)
    parents[x] = y


for _ in range(M):
    v, u = map(lambda x: int(x)-1, input().split())
    union(v, u)

weights = []
for d in dist:
    v, u, w = d
    if find(v) != find(u):
        weights.append(w)
        union(v, u)

answer = sum(list(map(lambda e: e**0.5, weights)))
print("{0:.2f}".format(answer))



