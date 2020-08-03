# https://programmers.co.kr/learn/courses/30/lessons/60058


def solution(p):
    if p == "":
        return ""

    stack = [p[0]]
    i = 0
    while stack:
        i += 1
        if p[i] == p[0]:
            stack.append(p[i])
        else:
            stack.pop()

    if p[0] == '(':
        return p[:i+1] + solution(p[i+1:])
    else:
        tmp = ''.join(list(map(lambda e: '(' if e == ')' else ')', p[1:i])))
        return '(' + solution(p[i+1:]) + ')' + tmp


print(solution(input()))