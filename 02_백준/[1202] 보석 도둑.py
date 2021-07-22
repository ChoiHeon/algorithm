# https://www.acmicpc.net/problem/1007


"""
* 사용한 알고리즘
    - 이분탐색
    - 유니온 파인드

* 로직
    1. 보석을 값비싸고 가벼운 순서로 정렬합니다.
    2. 가방의 무게를 오름차순으로 정렬합니다.
    3. 정렬된 보석들 중 가장 비싼 보석의 무게에 대해 아래의 과정을 반복합니다.
        a. 보석의 무게가 가장 큰(많은 무게를 담을 수 있는) 가방에 들어가지 않는다면 다음 보석으로 넘어갑니다.
        b. 보석이 들어갈 수 있는 가방 중 가장 작은 가방의 인덱스를 이분탐색을 아용해 찾습니다.
        c. 이미 인덱스가 사용되었다면 그보다 더 큰 가방을 확인합니다. 이 과정에서 유니온 파인드를 사용합니다.
        d. 사용할 수 있는 가방이 없다면 다음 보석으로 넘어갑니다.
        e. 보석의 값을 answer에 추가한 다음, 사용한 가방이 다음으로 큰 가방을 가리키도록 합니다.
    4. 담은 보석의 개수가 k개일 때, (3)번 과정을 종료합니다.
    5. answer의 원소들의 합을 출력합니다.
"""


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, k = map(int, input().split())
jewel = [[*map(int, input().split())] for _ in range(n)]
bag = [int(input()) for _ in range(k)]
used = [*range(k+1)]
answer = []

jewel.sort(key=lambda e: (-e[1], e[0]))
bag.sort()


def find(x):
    if x == used[x]:
        return x
    used[x] = find(used[x])
    return used[x]


for m, v in jewel:
    if len(answer) == k:
        break
    if bag[-1] < m:
        continue

    low, high = 0, k
    while low < high:
        mid = (low + high) // 2
        if m <= bag[mid]:
            high = mid
        else:
            low = mid + 1

    high = find(high)
    if high == k:
        continue
    used[high] += 1
    answer.append(v)

print(sum(answer))


