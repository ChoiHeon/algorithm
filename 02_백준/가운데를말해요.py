# https://www.acmicpc.net/problem/1655

"""
heap의 시간복잡도를 주의
heapq.heappush  --> O(log N)
heapq.heappop   --> O(log N)
heapq.heapify   --> O(N)
"""

########################################################################################################################

"""
첫 번째 코드의 경우 시간 복잡도가 (N^2) x (log N)
N은 최대 100,000 이므로 N^2일 경우 100억. 즉 100초 가량을 필요로 한다
"""
'''
import sys
import heapq
import math

heap = []
for i in range(int(sys.stdin.readline())):
    e = int(sys.stdin.readline())
    heapq.heappush(heap, e)
    temp = heap.copy()
    for _ in range(math.ceil((i+1)/2)):
        answer = heapq.heappop(temp)
    print(answer)
'''

########################################################################################################################

"""
두 번째 코드의 경우 오직 값의 중간값 만을 고려하기 위해 최대힙과 최소힙을 사용한다.
입력값의 크기를 고려하여 두 힙 중 하나를 선택할 때,
힙의 크기가 서로 균등하게 유지되도록 한다
"""

import sys
import heapq

right_heap = [10001]
left_heap = [(10001, -10001)]
flag = True

for _ in range(int(sys.stdin.readline())):
    p = int(sys.stdin.readline())

    if flag:
        if p > right_heap[0]:
            q = heapq.heappop(right_heap)
            heapq.heappush(left_heap, (-q, q))
            heapq.heappush(right_heap, p)
        else:
            heapq.heappush(left_heap, (-p, p))
    else:
        if p < left_heap[0][1]:
            q = heapq.heappop(left_heap)[1]
            heapq.heappush(right_heap, q)
            heapq.heappush(left_heap, (-p, p))
        else:
            heapq.heappush(right_heap, p)

    print(left_heap[0][1])
    flag = not flag
