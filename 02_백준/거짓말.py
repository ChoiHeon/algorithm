# https://www.acmicpc.net/problem/1043

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
t = [-1]*n
for i in [*map(lambda e: int(e)-1, input().split())][1:]: t[i] = 1
p = [[*map(lambda e: int(e)-1, input().split()[1:])] for _ in range(m)]
answer = -1


def party(k, state, count):
    global answer
    if k == m:
        answer = max(answer, count)
        return

    # 진실을 얘기할 때
    copied = state.copy()
    for i in p[k]:
        if copied[i] == 0:
            break
        copied[i] = 1
    else:  # 아무런 문제가 없었을 때
        party(k+1, copied, count)

    # 거짓을 얘기할 때
    copied = state.copy()
    for i in p[k]:
        if copied[i] == 1:
            break
        copied[i] = 0
    else:
        party(k+1, copied, count+1)


party(0, t, 0)
print(answer)


