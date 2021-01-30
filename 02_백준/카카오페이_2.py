# https://www.acmicpc.net/problem/11866


"""
* 정답의 경우의 수가 많은 문제
    1) 입금 / 잔액이 올바르지 않을 경우
    2) 출금 / 충전 X / 잔액이 올바르지 않을 경우
    3) 출금 / 충전 O / M에 의해 생길 수 없는 잔액이 있는 경우 (M보다 잔액이 클 경우)
    4) 출금 / 충전 O / M을 구할 수 없는 경우 (충전 금액의 최소 공배수가 1인 경우)
    5) 출금 / 충전 O / M을 구할 수 있고 잔액이 올바를 경우 (3번과 4번에 해당하지 않는 경우)
"""


import sys
input = sys.stdin.readline
x = t = z = 0
def f(u, v):
    while u:
        u, v = v % u, u
    return v
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a > 0:
        x += a
        if x != b:
            print(-1)
            exit()
    else:
        x += a
        if x < 0:
            t = f(t, b - x)
            z = max(z, b)
            x = b
        elif x != b:
            print(-1)
            exit()
if not t:
    t = 1
print(t if t > z else -1)