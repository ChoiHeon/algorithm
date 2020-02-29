# https://www.acmicpc.net/problem/4195


"""
기본적인 유니온 파인드에서
트리(부분집합)의 크기에 대한 정보를 기록하도록 구조를 변경

인덱스 i에 대한 parents[i]를 (-i -1)로 초기화
이후 트리의 루트는 항상 해당 트리의 노드의 개수를 저장한다
--> 노드 개수 = -(x - parents[x])

find 함수의 루트를 찾는 조건를 달리하고
union 함수의 x와 y가 같은 트리에 있는지 여부에 따라 다르게 처리하고도록 구현한다

ps) parents 를 {}로 구현하여 문자열를 정수로 변경하는 과정을 거치지 않고
    바로 parents[문자열]를 통해 접근이 가능하다
"""


import sys
_input = sys.stdin.readline


def find(parents, x):
    if parents[x] < 0:
        return x
    parents[x] = find(parents, parents[x])
    return parents[x]


def node_count(parents, x):
    x = find(parents, x)
    return -(x+parents[x])


def union(parents, x, y):
    x = find(parents, x)
    y = find(parents, y)
    if x != y:
        parents[x] -= node_count(parents, y)
        parents[y] = x
    return node_count(parents, x)


for _ in range(int(_input())):
    parents = []
    friends = {}
    cnt = 0
    for __ in range(int(_input())):
        A, B = _input().split()
        for P in [A, B]:
            if P not in friends.keys():
                friends[P] = cnt
                parents.append(-cnt-1)
                cnt += 1
        A, B = friends[A], friends[B]
        print(union(parents, A, B))
