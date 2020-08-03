# https://www.acmicpc.net/problem/10816

from collections import *

input()
d = Counter(input().split())
input()
print(*(d[e] for e in input().split()))  # 없는 e에 대해서 0을 반환

