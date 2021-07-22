# https://www.acmicpc.net/problem/1931

import sys

i = sys.stdin.readline
m = [list(map(int, i().split())) for _ in range(int(i()))]
m = sorted(m, key=lambda t: t[0])
m = sorted(m, key=lambda t: t[1])

s = 0
ret = 0

for t in m:
    if t[0] >= s:
        s = t[1]
        ret += 1

print(ret)

'''
# wrong solution
for t in m[1:]:
    if(s <= t[0]):
        e = min(e, t[1])
        if t[0] >= e:
            ret += 1
            s = e
            e = t[1]

print(ret)
'''


    
