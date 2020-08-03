# coding=utf-8
# https://programmers.co.kr/learn/courses/30/lessons/42890


"""
* combination 대신에 비트 사용 가능
ex) n_col 이 4일 경우, 0 ~ 2^4-1의 비트로 표현 가능
"""


from itertools import combinations
from collections import deque


def solution(relation):
    n_col = len(relation[0])
    n_row = len(relation)
    idx_list = list(range(n_col))
    super_keys = deque()

    for n in range(1, n_col+1):
        for idx in combinations(idx_list, n):
            rows = set()
            for i in range(n_row):
                rows.add(tuple([relation[i][j] for j in idx]))
            if len(rows) == n_row:
                super_keys.append(idx)

    answer = 0
    while super_keys:
        super_key = super_keys.popleft()
        answer += 1
        for key in super_keys.copy():
            if set(super_key) <= set(key):
                super_keys.remove(key)

    return answer


input_data = eval(input())
print(solution(input_data))
