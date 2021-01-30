# coding=utf-8
# https://programmers.co.kr/learn/courses/30/lessons/42892


import sys
sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.left = None
        self.right = None

    def get_pos(self):
        return (self.x, self.y, )


def pre_order(head, index):
    if not head:
        return []
    return [index[head.get_pos()]] + pre_order(head.left, index) + pre_order(head.right, index)


def post_order(head, index):
    if not head:
        return []
    return post_order(head.left, index) + post_order(head.right, index) + [index[head.get_pos()]]


def solution(nodeinfo):
    index = dict()
    for i in range(len(nodeinfo)):
        index[tuple(nodeinfo[i])] = i+1

    nodeinfo.sort(key=lambda e: (e[1], -e[0]))
    head = Node(*nodeinfo.pop())
    level = [head.y]

    while nodeinfo:
        node = Node(*nodeinfo.pop())
        if level[-1] != node.y:
            level.append(node.y)
        cursor = head
        while cursor.y != level[-2]:
            cursor = cursor.left if cursor.x > node.x else cursor.right
        if cursor.x > node.x:
            cursor.left = node
        else:
            cursor.right = node

    return [pre_order(head, index), post_order(head, index)]

input_data = input()
print(solution(eval(input_data)))