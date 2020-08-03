# https://www.acmicpc.net/problem/10775


"""
유니온 파인드를 통해 도킹 가능 여부를 판단하는 코드
i 번째 게이트에 비행기가 도킹했을 경우
다음에 i 번째 게이트에 도킹을 시도하는 비행기가 자연스럽게 i-1 번째 게이트에 도킹을 시도하도록
유니온 파인드를 통해 (i)와 (i-1)을 연결한다

이 때, 도착한 비행기가 j 번째 게이트에 도킹하고자 할 때
유니온 파인드를 통해 반환된 게이트 번호가 0일 경우
해당 비행기가 도킹 가능한 게이트가 없다는 의미이므로
답을 반환하고 프로그램을 종료시킨다

ps) 문제의 문장들 중 애매하게 해석되는 문장이 있어서 해맸던 문제...
"""


import sys


def find(parents, x):
    if parents[x] == x:
        return x
    parents[x] = find(parents, parents[x])
    return parents[x]


def union(parents, x, y):
    x = find(parents, x)
    y = find(parents, y)
    parents[x] = y


_input = sys.stdin.readline
g = [*range(int(_input())+1)]
ans = 0

for _ in range(int(_input())):
    i = find(g, int(_input()))
    if not i:
        break
    ans += 1
    union(g, i, i-1)

print(ans)