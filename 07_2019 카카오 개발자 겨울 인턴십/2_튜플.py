# https://programmers.co.kr/learn/courses/30/lessons/64065


def solution(s):
    import re
    set_list = re.findall("{.+?}", s[1:-1])
    set_list = [set()] + sorted(list(map(eval, set_list)), key=len)

    answer = []
    for i in range(len(set_list) - 1):
        answer.append(*(set_list[i+1] - set_list[i]))

    return answer



print(solution(eval(input())))
