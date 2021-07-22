# https://www.acmicpc.net/problem/1654

k, n = map(int, input().split())
p = [int(input()) for _ in range(k)]
low, high = 1, max(p)
ans = float('-inf')

while low <= high:
    mid = (low + high) // 2
    temp = sum(map(lambda e: e // mid, p))

    print(mid)

    if temp < n:
        high = mid - 1
    else:
        low = mid + 1
        ans = max(ans, mid)

print(ans)