# 미로 탈출
# https://programmers.co.kr/learn/courses/30/lessons/81304

def solution(n, start, end, roads, traps):
    import heapq

    m = len(traps)
    start, end = start - 1, end - 1
    traps = [e - 1 for e in traps]
    edges = [[] for _ in range(n)]
    board = [[-1] * n for _ in range(n)]
    trap_id = {traps[i]: i for i in range(m)}
    visited = [set() for _ in range(1 << m)]

    for p, q, s in roads:
        edges[p - 1].append(q - 1)
        edges[q - 1].append(p - 1)
        board[p - 1][q - 1] = s

    heap = [[0, start, 0]]  # { 총 이동한 거리, 현재 노드, 트랩 방문 여부 }

    while heap:
        t, p, v = heapq.heappop(heap)

        if p in visited[v]:
            continue
        if p == end:
            return t

        visited[v].add(p)
        f1 = p in trap_id.keys() and bool(v & (1 << trap_id[p]))

        for q in edges[p]:

            f2 = q in trap_id.keys() and bool(v & (1 << trap_id[q]))
            if f1 ^ f2:
                if board[q][p] != -1:
                    if q in trap_id.keys():
                        heapq.heappush(heap, [t + board[q][p], q, v ^ (1 << trap_id[q])])
                    else:
                        heapq.heappush(heap, [t + board[q][p], q, v])
            else:
                if board[p][q] != -1:
                    if q in trap_id.keys():
                        heapq.heappush(heap, [t + board[p][q], q, v ^ (1 << trap_id[q])])
                    else:
                        heapq.heappush(heap, [t + board[p][q], q, v])

    return -1