# https://programmers.co.kr/learn/courses/30/lessons/60062


"""
* 친구를 최소 횟수로 사용해야 하기 때문에, 길이가 가 긴 친구를 우선하여 확인하는 것이 옳음
* 반시계 방향으로 이동이 가능하지만 고려할 필요가 없음
    - 반시계 방향으로 b -> a 이동이 가능하다면, 시계 방향으로 a -> b 이동이 가능하기 때문
    - 즉, 시계 방향만 고려하면 됨

* 수정한 부분:
    - 점검 길이가 긴 순서대로 뽑고 수열을 계산하여 체크하였음
    ex. [4, 3, 2]  -->  [2, 3, 4] [2, 4, 3] [3, 4, 2] [3, 2, 4] ......
"""


from collections import deque
from itertools import permutations


def repair(n, weak, d):
    s = weak[0]
    for i in weak.copy():
        v = (i-s) if s <= i else (i-s+n)
        if v > d:
            return False
        weak.popleft()
    return True


def solution(n, weak, dist):
    dist.sort(reverse=True)
    l_weak = [weak[i:]+weak[:i] for i in range(len(weak))]

    for i in range(1, len(dist)+1):
        p_dist = permutations(dist[:i])
        for sub_dist in p_dist:
            for sub_weak in l_weak:
                deq_weak = deque(sub_weak)
                for d in sub_dist:
                    if repair(n, deq_weak, d):
                        return i
    return -1


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
