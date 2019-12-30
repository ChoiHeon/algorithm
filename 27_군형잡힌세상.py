# https://www.acmicpc.net/problem/9372

import sys


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, entry):
        self.stack.append(entry)

    def pop(self):
        if self.is_empty():
            return -1
        return self.stack.pop()

    def clear(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False


while True:
    text = sys.stdin.readline()
    ret = True
    stack = Stack()

    if text == ".":
        break

    for ch in text:
        if ch == '(' or ch == '{' or ch == '[':
            stack.push(ch)

        elif ch == ')':
            if stack.pop() != '(':
                ret = False
        elif ch == '}':
            if stack.pop() != '{':
                ret = False
        elif ch == ']':
            if stack.pop() != '[':
                ret = False

    print("yes" if ret else "no")