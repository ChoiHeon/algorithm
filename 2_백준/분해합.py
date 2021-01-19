# https://www.acmicpc.net/problem/https://www.acmicpc.net/problem/2231


import sys


def digit_generator(x):
    ret = x
    while x != 0:
        ret += x % 10
        x = x // 10
    return ret


N = sys.stdin.readline()
T = 0

if len(N)-1 > 2:
    T = (len(N)-1) * 10

N = int(N)
M = N-T
answer = 0
for _ in range(T):
    if digit_generator(M) == N:
        answer = M
        break
    M += 1

print(answer)
