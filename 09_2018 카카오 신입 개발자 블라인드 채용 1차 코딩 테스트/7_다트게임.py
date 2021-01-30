# https://programmers.co.kr/learn/courses/30/lessons/17681


def solution(dartResult):
    import re

    score = re.findall('\d+', dartResult)
    option = re.findall('[^\d]+', dartResult)

    bonus = dict()
    bonus['S'] = 1; bonus['D'] = 2; bonus['T'] = 3

    total = []
    for i in range(len(score)):
        total.append(int(score[i]) ** bonus[option[i][0]])
        if len(option[i]) < 2:
            continue

        if option[i][1] == '#':
            total[-1] *= -1
        else:
            total[-1] *= 2
            if i != 0:
                total[-2] *= 2

    return sum(total)


print(solution(eval(input())))
