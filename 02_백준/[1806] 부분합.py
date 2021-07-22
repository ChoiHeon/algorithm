# https://www.acmicpc.net/problem/1806


def solution(n, s, arr):
    total = arr[0]
    ret = float('inf')
    start, end = 0, 1

    while end <= n:
        if total < s:
            if end < n:
                total += arr[end]
            end += 1
        else:
            ret = min(ret, end-start)
            total -= arr[start]
            start += 1

    return ret if ret != float('inf') else 0


n, s = map(int, input().split())
arr = [*map(int, input().split())]
print(solution(n, s, arr))
