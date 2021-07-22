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


def gcd(p, q):
    while q:
        p, q = q, p & q
    return p


N = int(input())
a = [0] * 3000001
b = [0] * 3000001
answer = 0

for i in range(1, N+1):
    a[i], b[i] = map(int, input().split())
    answer = gcd(answer, b[i]-b[i-1]-a[i])

for i in range(1, N+1):
    if b[i]-b[i-1] == a[i]:
        continue
    if (answer and answer <= b[i]) or (a[i] > 0) or (a[i] < 0 and -a[i] < b[i-1]):
        print(-1)
        sys.exit(0)

print(answer) if answer else print(1)