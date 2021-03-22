# https://www.acmicpc.net/problem/1916


"""
* 벨만포드 알고리즘
    그래프에서 시작 정점으로부터 다른 모든 정점까지의 최단 경로를 찾기 위한 알고리즘이다
    음수 가중치가 존재해도 사용이 가능하며 음수 사이클도 회피할 수 있다

* 음수 사이클 회피 방법
    정점의 개수가 N개 일 때, 시작 정점에서 특정 정점까지 최대 N-1개의 간선을 거칠 수 있으므로
    인접 간전을 검사하고 거리 값을 갱신하는 과정을 N-1번으로 제한한다
    경로에 N번 째 간선이 추가되면 사이클이 생겼다고 판단할 수 있다

* 알고리즘 과정
    1. 시작 정점 V를 정한다
    2. V에서 나머지 정점까지의 거리를 무한대로 설정한다. (자기자신인 V까지 거리는 0)
    3. 현재 정점의 모든 인접 정점(U)을 탐색, 현재까지 기록된 거리가 U를 거쳐서 가능한 거리보다 길다면 갱신
        D[W] = min(D[W], D[U] + E[U][W])
    4. 3번 과정을 N-1번 거친다.
    5. 만약 N번 째에서 거리가 갱신될 경우, 음수 사이클이 존재함을 확인할 수 있다.

* 추가
    거리가 갱신될 때 마다 (V -> U) 정점 U 이전에 V가 있다는 것을 기록하면 최단 경로를 알 수 있다

* 시간복잡도
    O(VE)   (V: 정점의 개수 / E: 간선의 개수)
"""


n = int(input())
m = int(input())
edges = {i : [] for i in range(n)}
for _ in range(m):
    v, u, c = map(lambda e: int(e)-1, input().split())
    edges[v].append((u, c+1))
f, t = map(lambda e: int(e)-1, input().split())

# 시작 정점을 제외한 나머지 정점까지의 거리를 무한대로 초기화
dist = [float('inf')] * n
dist[f] = 0

# (정점의 개수 - 1)번 만큼 거리를 갱신
for _ in range(n-1):
    for v in range(n):
        for u, c in edges[v]:
            dist[u] = min(dist[u], dist[v]+c)
    print(dist)

# 음수 사이클 존재 확인
for v in range(n):
    for u, c in edges[v]:
        if dist[u] > dist[v] + c:
            print("음수 사이클이 존재합니다.")
            exit(0)

print(dist[t])





