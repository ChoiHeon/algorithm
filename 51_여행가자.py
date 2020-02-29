# https://www.acmicpc.net/problem/1976


"""
특정 두 노드 사이에 다른 노드의 경유가 가능한 경로가 있는지 여부를 확인하는 문제
유니온 파인드를 통해 두 노드의 최상위 부모 노드의 동일 여부를 확인하여
같은 그래프 내에 있는지 확인하여 해결이 가능하다
"""


import sys
parents = []


def get_parent(x):
    global parents
    if parents[x] == x:
        return x
    parents[x] = get_parent(parents[x])
    return parents[x]


def union(x, y):
    global parents
    x = parents[x]
    y = parents[y]
    parents[x] = y


n = int(sys.stdin.readline())
parents = list(range(n))
m = int(sys.stdin.readline())
for i in range(n):
    path = list(map(int, sys.stdin.readline().split()))
    for j in path:
        if j == 1:
            union(i, j)

plan = list(map(lambda x: get_parent(int(x)-1), sys.stdin.readline().split()))
answer = True
for s in range(m-1):
    if plan[s] != plan[s+1]:
        answer = False
        break

print("YES") if answer else print("NO")