# https://www.acmicpc.net/problem/2512


n = int(input())
costs = [*map(int, input().split())]
m = int(input())
start, end = 1, max(costs) + 1
mid = -1

while start < end:
    mid = (start + end) // 2
    total = sum(map(lambda e: min(e, mid), costs))

    """
    아래의 조건식으로 인해 end의 값으로 만들 수 있는 합은
    무조건 m보다 아주 작은 차이로 크다.
    해당 알고리즘의 m보다 작으면서 최대 값을 찾는 것이므로
    알고리즘의 해는 end-1 이다.
    """
    if total > m:
        end = mid
    else:
        start = mid + 1

print(end - 1)