# https://programmers.co.kr/learn/courses/30/lessons/43163


from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0

    n = len(begin)
    stack = deque([(begin, {*words}, 0)])

    while stack:
        current, sub, cnt = stack.popleft()
        for word in sub:
            diff = 0
            for i in range(n):
                if current[i] != word[i]:
                    diff += 1
            if diff != 1:
                continue
            if word == target:
                return cnt+1
            stack.append((word, sub - {word}, cnt+1))
    return 0



print(solution(eval(input()), eval(input()), eval(input())))