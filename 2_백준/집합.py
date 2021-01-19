# https://www.acmicpc.net/problem/11723


"""
* 문자열 비교에 시간이 많이 걸리므로 해쉬코드를 이용해 비교하는 딕셔너리를 사용
* 각 문자열에 많는 동작을 림다식을 통해 미리 정의
"""

import sys
input = sys.stdin.readline

c = dict()
c["add"] = lambda s, x: s.add(x)
c["remove"] = lambda s, x: s.remove(x) if x in s else None
c["check"] = lambda s, x: print(1 if x in s else 0)
c["toggle"] = lambda s, x: s.remove(x) if x in s else s.add(x)
c["all"] = set(range(1, 21))
c["empty"] = set()

s = set()
for _ in range(int(input())):
    info = input().split()
    if len(info) == 1:
        s = c[info[0]]
    else:
        c[info[0]](s, int(info[1]))
