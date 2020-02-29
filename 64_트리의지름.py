# https://www.acmicpc.net/source/8726628


"""
트리구조의 특성을 활용
임의의 정점에서 가장 먼 정점 A를 탐색
A에서 가장 먼 정점 B 까지의 거리를 구하는 문제
"""


import sys, copy
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
dist = [-1] * (N+1)

for _ in range(N):
    info = list(map(int, input().split()))

    for i in range(1, len(info)-1, 2):
        graph[info[0]].append([info[i], info[i+1]])


def tree_diameter(p, v, d):
    global graph, dist
    dist[v] = d

    for u, c in graph[v]:
        if u != p:
            tree_diameter(v, u, d+c)


tree_diameter(-1, 1, 0)
tree_diameter(-1, dist.index(max(dist)), 0)
print(max(dist))
