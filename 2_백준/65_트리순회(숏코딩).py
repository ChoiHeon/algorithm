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

dic = {}
for _ in range(int(input())):
    info = input().split()
    dic[info[0]] = info[1], info[2]

pre_order = ""
in_order = ""
post_order = ""


def traversal(root):
    global pre_order, in_order, post_order

    if root == '.':
        return

    pre_order += root
    traversal(dic[root][0])

    in_order += root
    traversal(dic[root][1])

    post_order += root


traversal('A')
print(pre_order)
print(in_order)
print(post_order)
