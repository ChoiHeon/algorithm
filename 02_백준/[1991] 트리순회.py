# https://www.acmicpc.net/problem/1991


"""
이진트리 탐색방법 3가지
1) 전위 순회: 루트 / 왼쪽 / 오른쪽
2) 중위 순회: 왼쪽 / 루트 / 오른쪽
3) 후위 순회: 왼쪽/ 오른쪽 / 루트
"""


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
left = [0] * N
right = [0] * N
KEY = ord('A')

for _ in range(N):
    parent, l_child, r_child = map(lambda c: ord(c) - KEY, input().split())
    if chr(l_child + KEY) != '.':
        left[parent] = l_child
    if chr(r_child + KEY) != '.':
        right[parent] = r_child


def pre_traversal(root):
    print(chr(root + KEY), end='')      # root
    if left[root]:                      # left child
        pre_traversal(left[root])
    if right[root]:                     # right child
        pre_traversal(right[root])


def in_traversal(root):
    if left[root]:                      # left child
        in_traversal(left[root])
    print(chr(root + KEY), end='')      # root
    if right[root]:                     # right child
        in_traversal(right[root])


def post_traversal(root):
    if left[root]:                      # left child
        post_traversal(left[root])
    if right[root]:                     # right child
        post_traversal(right[root])
    print(chr(root + KEY), end='')      # root


pre_traversal(0)
print()
in_traversal(0)
print()
post_traversal(0)

