# https://programmers.co.kr/learn/courses/30/lessons/72412


"""
리스트의 원소가 전부 정수이고 정렬되어있다고 가정할 경우,
임의의 값 이하 또는 이상인 원소의 개수를 찾을 땐, 이분탐색이 제일 효율적
"""


from collections import defaultdict
from itertools import product
import bisect


def solution(info, query):
    group = defaultdict(list)

    for i in range(len(info)):
        info[i] = info[i].split()

        lang = [info[i][0], '-']
        job = [info[i][1], '-']
        career = [info[i][2], '-']
        food = [info[i][3], '-']
        score = int(info[i][4])

        for case in product(lang, job, career, food):
            group[case].append(score)

    for case in group.keys():
        group[case].sort(key=lambda e: -e)

    answer = []
    for q in query:
        q = q.split()
        case = (q[0], q[2], q[4], q[6])
        boundary = int(q[7])
        count = len(group[case]) - bisect.bisect_left(group[case], boundary)
        answer.append(count)

    return answer


print(solution(eval(input()), eval(input())))
