# https://www.acmicpc.net/problem/15956


"""
<벨만 포드 알고리즘>
기본 원리)  그래프에 노드가 V개가 있을 경우, 노드 i에서 j까지 최단거리를 구할 때
            지날 수 있는 edge의 최대 개수는 V-1개이다. V개 이상일 경우 사이클을을 돌았음을 의미하기 때문

음의 사이클) 이 때, V개 이상의 edge를 지났을 때 최단거리를 구했을 경우
            아는 음의 사이클을 돌았음을 의미한다 (음의 사이클을 돌 경우 비용이 감소하기 때문이다)

파이썬의 float('inf')는
float('inf') -1 < float('inf')를 실행시
False를 반환한다
즉, 현재 최단거리가 무한대일 경우를 배제하는 것이 좋다(파이썬은 별도로 구현하지 않아도 동작한다)
"""


"""
구현 방법2) 모든 edge(시작점, 도착점, 비용)을 저장
            V-1번 만큼 모든 edge를 통해 최단거리를 갱신한다(갱신방법은 다익스트라 알고리즘과 동일 / 이미 확인한 노드를 체크할 필욘 없음)
            한 번 더 각 노드에 대한 최간거리를 갱신될 수 있는지 확인, 갱신될 경우 음의 사이클을 돌았음을 의미한다
            
구현 방법1과 그래프 저장 방법에서 차이를 보이며 
구현 방법2가 약 4배 빠르다
"""


import sys
input = sys.stdin.readline


v, e = map(int, input().split())
dist = [0] + [float('inf')] * (v-1)
edges = []
cycle = False

for _ in range(e):
    edge = list(map(int, input().split()))
    edges.append([edge[0]-1, edge[1]-1, edge[2]])

for i in range(v):
    for start, end, cost in edges:
        if dist[end] > dist[start] + cost:
            dist[end] = dist[start] + cost
            if i == v-1:
                cycle = True

if cycle:
    print(-1)
else:
    for ans in dist[1:]:
        print(ans) if ans != float('inf') else print(-1)