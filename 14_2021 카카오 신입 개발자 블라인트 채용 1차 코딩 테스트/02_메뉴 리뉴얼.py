# https://programmers.co.kr/learn/courses/30/lessons/72411


from itertools import combinations
from collections import Counter


def solution(orders, course):
    combs = []
    answer = []

    orders = [*map(sorted, orders)]
    for cnt in course:
        combs.append([])
        for order in orders:
            order = ''.join(sorted(order))
            combs[-1] += [*map(''.join, combinations(order, cnt))]

    combs = [*map(lambda comb: Counter(comb).most_common(), combs)]

    for comb in combs:
        if not comb:
            continue

        max_cnt = comb[0][1]
        for foods, cnt in comb:
            if cnt == 1:
                continue
            if cnt != max_cnt:
                break
            answer.append(foods)

    return sorted(answer)


print(solution(eval(input()), eval(input())))