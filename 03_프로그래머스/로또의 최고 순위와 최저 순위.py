# https://programmers.co.kr/learn/courses/30/lessons/77484


def solution(lottos, win_nums):
    unknown = lottos.count(0)
    consist = len([n for n in lottos if n in win_nums])

    return [*map(lambda e: 7-e if e > 1 else 6, [unknown+consist, consist])]