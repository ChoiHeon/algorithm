# https://programmers.co.kr/learn/courses/30/lessons/12979


import math


def solution(n, stations, w):
    answer = 0
    outers = [(0, n)]
    v = 2 * w + 1

    for station in stations:
        station -= 1
        start, length = outers.pop()
        outers.append((start, max(station - w - start, 0)))
        outers.append((station + w + 1, max(length + start - station - w - 1, 0)))

    for outer in outers:
        answer += math.ceil(outer[1] / v)

    return answer


# test
print(solution(eval(input()), eval(input()), eval(input())))