# https://www.acmicpc.net/problem/12869


from itertools import permutations
from collections import deque

n = int(input())
scv = [*map(int, input().split())]
dam = [9, 3, 1]
answer = -1
dupl = set()
queue = deque()

dupl.add(tuple(scv))
queue.append((scv, 0))
while queue:
    hp, cnt = queue.popleft()
    if not hp:
        answer = cnt
        break

    for case in permutations(hp):
        case = [*case]
        for i in range(len(case)):
            case[i] -= dam[i]
        case = [*filter(lambda e: e > 0, case)]
        if tuple(case) not in dupl:
            dupl.add(tuple(case))
            queue.append((case, cnt+1))

print(answer)


"""
이외에 방법으로는
dp[61][61][61]을 이용해 각 상태의 횟수를 저장하면 더 빠르게 탐색 가능
"""