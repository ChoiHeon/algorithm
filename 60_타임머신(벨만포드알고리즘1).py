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
구현 방법1) 모든 노드에 대한 연결된 edge를 저장한다 
            V-1번 만큼 각 노드와 edge를 통해 최단거리를 갱신한다(갱신방법은 다익스트라 알고리즘과 동일 / 이미 확인한 노드를 체크할 필욘 없음)
            한 번 더 각 노드에 대한 최간거리를 갱신될 수 있는지 확인, 갱신될 경우 음의 사이클을 돌았음을 의미한다
"""


import sys
input = sys.stdin.readline


v, e = map(int, input().split())
graph = [[] for _ in range(v)]
dist = [0] + [float('inf')] * (v-1)
neg_cycle = False

for _ in range(e):
    start, end, cost = map(int, input().split())
    graph[start-1].append([end-1, cost])

for cnt in range(v):
    for start in range(v):
        for end, cost in graph[start]:
            if dist[start] != float('inf') and dist[end] > dist[start] + cost:
                dist[end] = min(dist[end], dist[start] + cost)
                if cnt == v-1:
                    neg_cycle = True

if neg_cycle:
    print(-1)
else:
    for ans in dist[1:]:
        print(ans) if ans != float('inf') else print(-1)