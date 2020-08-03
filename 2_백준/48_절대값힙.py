# https://www.acmicpc.net/problem/11286

"""
입력의 길이가 길지 않은 것 같지만,
input 대신 sys.stdin.readline 함수를 쓰지 않을 경우 시간초과가 발생
앞으로 가급적이면 input 함수의 사용을 지양할 것

파이썬에서 heap 구조를 구현하지 위해서 heapq 모듈을 import
이 모듈은 기본적으로 min heap 만을 지원하므로 tuple을 push
이때 정렬을 앞의 원소부터 차례로 하므로 다양한 방식의 heap의 구현이 가능
"""


import sys, heapq


A = []
for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(A, (abs(x), x))
    else:
        print(heapq.heappop(A)[1]) if A else print(0)
