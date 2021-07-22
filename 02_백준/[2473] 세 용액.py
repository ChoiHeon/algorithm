# https://www.acmicpc.net/problem/2473


"""
visited를 이용해 중복을 제거해서 빠른 성능을 보임
하지만 visited에 저장되는 만큼 메모리 자원을 사용함
"""


import sys
sys.setrecursionlimit(10**6)

I = sys.stdin.readline
n = int(I())
liq = sorted(map(int, I().split()))
visited = set()
answer = [(-1, -1, -1), float('inf')]


def sol(low, mid, high):
    global answer
    a, b, c = liq[low], liq[mid] ,liq[high]
    r = a + b + c

    if r == 0:
        print(a, b, c)
        exit(0)
    elif abs(r) < answer[1]:
        answer[0] = (a, b, c)
        answer[1] = abs(r)

    if r < 0:
        # move low
        if low < mid - 1 and (low + 1, mid, high) not in visited:
            visited.add((low + 1, mid, high)); sol(low + 1, mid, high)
        # move mid
        if mid + 1 < high and (low, mid + 1, high) not in visited:
            visited.add((low, mid + 1, high)); sol(low, mid + 1, high)
    else:
        # move mid
        if mid - 1 > low and (low, mid - 1, high) not in visited:
            visited.add((low, mid - 1, high)); sol(low, mid - 1, high)
        # move high
        if mid < high - 1 and (low, mid, high - 1) not in visited:
            visited.add((low, mid, high - 1)); sol(low, mid, high - 1)


low, mid, high = 0, n // 2, n-1
visited.add((low, mid, high))
sol(low, mid, high)

print(*answer[0])

