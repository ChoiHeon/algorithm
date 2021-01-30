# https://programmers.co.kr/learn/courses/30/lessons/67258


"""
* 투 포인터 알고리즘을 사용
    - 조건을 만족할 경우 시작점을 앞으로
    - 조건을 만족하지 못할 경우 끝점을 뒤로

* 리스트를 집합으로 바꿀 경우 시간초과가 발생
"""

def solution(gems):
    from collections import Counter

    n, m = len(gems), len(set(gems))
    gem_counter = Counter()
    s, e = 0, 0
    answer = [0, n-1]

    gem_counter[gems[0]] = 1
    while True:
        if len(gem_counter.keys()) == m:
            if answer[1]-answer[0] > e-s or (answer[1]-answer[0] == e-s and e < answer[0]):
                answer = [s, e]
            if s == n-1:
                return [answer[0]+1, answer[1]+1]
            gem_counter[gems[s]] -= 1
            if gem_counter[gems[s]] == 0:
                del gem_counter[gems[s]]
            s += 1
        else:
            if e == n-1:
                return [answer[0]+1, answer[1]+1]
            e += 1
            gem_counter[gems[e]] += 1


print(solution(eval(input())))
