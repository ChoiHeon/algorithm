# https://www.acmicpc.net/problem/15956


"""
*DFS* 를 통한 트리 구조 생성
(함수 내부 구조에 따라 BFS도 가능)
"""


import sys
sys.setrecursionlimit(10**6)            # 재귀 제한 확장 (default value = 1000)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]        # 입력 받은 그리프를 저장
tree = [0] * (N+1)                      # 각 노드의 부모노드를 기록하여 트리로 생성

for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def create_tree(root):
    stack = [root]
    while stack:
        node = stack.pop()
        for child in graph[node]:
            tree[child] = node
            graph[child].remove(node)
            stack.append(child)


create_tree(1)
for answer in tree[2:]:
    print(answer)





