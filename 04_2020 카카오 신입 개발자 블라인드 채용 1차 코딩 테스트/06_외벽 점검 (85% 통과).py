# https://programmers.co.kr/learn/courses/30/lessons/60062


"""
* 친구를 최소 횟수로 사용해야 하기 때문에, 길이가 가 긴 친구를 우선하여 확인하는 것이 옳음
* 반시계 방향으로 이동이 가능하지만 고려할 필요가 없음
    - 반시계 방향으로 b -> a 이동이 가능하다면, 시계 방향으로 a -> b 이동이 가능하기 때문
    - 즉, 시계 방향만 고려하면 됨

* 일부 틀린 이유:
    - 예를 들어 친구들이 3, 2, 4 순서대로 점검할 때 최소가 가능할 경우
    - 4, 3, 2 (내림차순)으로 밖에 점검하지 않았음
"""


from collections import deque


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
    l_weak = [deque(weak[i:]+weak[:i]) for i in range(len(weak))]

    for i in range(len(dist)):
        for j in range(len(weak)):
            if repair(n, l_weak[j], dist[i]):
                return i+1
            print(l_weak)
    return -1


print(solution(4, [4], [1]))
