# https://programmers.co.kr/learn/courses/30/lessons/12984

"""
(블록 층, 비용) 그래프가 아래 방향으로 볼록한 그래프를 띄기 때문에
비용이 변하는 부분(극점)을 탐색하여 해를 찾을 수 있다.
"""

from itertools import chain


def solution(land, p, q):
    land = sorted([*chain(*land)])
    n = len(land)
    answer = cost = (sum(land) - land[0] * n) * q

    for i in range(1, n):
        cost += (land[i] - land[i - 1]) * i * p - (land[i] - land[i - 1]) * (n - i) * q
        if answer < cost:
            break
        answer = cost

    return answer


# 이분탐색 활용(시간초과)
"""
def solution(land, p, q):
    answer = float('inf')
    n = len(land)
    start = 0
    end = max(map(max, land))

    def cost(floor):
        ret = 0
        for i in range(n):
            for j in range(n):
                if land[i][j] < floor:
                    ret += (floor - land[i][j]) * p
                elif land[i][j] > floor:
                    ret += (land[i][j] - floor) * q
        return ret

    while  start < end:
        a = (start + end) // 2
        b = a + 1
        cost_a = cost(a)
        cost_b = cost(b)

        if cost_a == cost_b:
            return cost_a
        elif cost_a < cost_b:
            end = b
        else:
            start = a

    for c in range(start, end + 1):
        answer = min(answer, cost(c))

    return answer
"""


# text
print(solution(eval(input()), eval(input()), eval(input())))