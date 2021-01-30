# https://programmers.co.kr/learn/courses/30/lessons/67257


def solution(expression):
    import re
    from itertools import permutations
    from collections import deque

    digits = re.findall("\d+", expression)
    operators = re.findall("[^\d]", expression)
    cases = list(permutations(set(operators)))
    answer = -1

    for case in cases:
        d, op = deque(digits), deque(operators)
        for priority in case:
            for _ in range(len(op)):
                if op[0] == priority:
                    d.appendleft(str(eval(d.popleft() + op.popleft() + d.popleft())))
                else:
                    d.append(d.popleft())
                    op.append(op.popleft())
            d.append(d.popleft())
        answer = max(answer, eval("abs(%s)" % d[0]))

    return answer


print(solution(eval(input())))
