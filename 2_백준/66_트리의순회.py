# https://www.acmicpc.net/problem/2263


"""
결과적으로 Divide & Conquer 방법으로 해결
파이썬에서 dictionary를 사용하여 간단하게 list의 인자의 인덱스를 찾을 수 있음
"""


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
in_order = list(input().split())
post_order = list(input().split())
pre_order = []
dct = {}

for i in range(0, N):
    dct[in_order[i]] = i


def find_pre_order(x, y, p, q):
    root = post_order[q-1]
    pre_order.append(root)
    i = dct[root]

    if i != x:
        find_pre_order(x, i, p, p+i-x)
    if i != y-1:
        find_pre_order(i+1, y, p+i-x, q-1)


find_pre_order(0, N, 0, N)
print(" ".join(pre_order))






