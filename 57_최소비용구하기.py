# https://www.acmicpc.net/problem/1916


"""
방향과 가중치가 주어진 그래프에 대하여
특정 정점에 대한 나머지 정점들의 최단거리를 구하는 문제
--> 다익스트라 알고리즘

다익스트라 알고리즘 (힙 사용)
1. 출발지 A를 입력 받는다
2. heap 에 (0, A)를 입력한다 --> 앞의 원소를 먼저 정렬의 기준으로 삼으므로 순서에 주의
3. heap 이 빌 때까지 while 문 실행
3_1. pop 하여 얻은 가중치(첫 번째 원소)가 dp의 가중치보다 클 경우 continue
3_2. 얻은 노드(두 번째 원소)와 연결된 노드에 대한 가중치를 더한 값이 (wei + next_wei)이 dp의 wei보다 작을 경우 갱신
     --> dp의 가중치를 변경하고 heap 에 push
"""

import sys, heapq
input = sys.stdin.readline

cities = int(input())
buses = int(input())
graph = [[]*cities for _ in range(cities)]      # [start][end, cost]

for _ in range(buses):
    start, end, cost = map(int, input().split())
    graph[start-1].append([end-1, cost])

A, B = map(lambda x: int(x)-1, input().split())

min_costs = [float("inf")] * cities
heap = [(0, A)]     # [(cost, city)]
min_costs[A] = 0

while heap:
    cost, city = heapq.heappop(heap)
    if cost > min_costs[city]:
        continue

    for next_city, next_cost in graph[city]:
        if min_costs[next_city] > cost + next_cost:
            min_costs[next_city] = cost + next_cost
            heapq.heappush(heap, (min_costs[next_city], next_city))

print(min_costs[B])
