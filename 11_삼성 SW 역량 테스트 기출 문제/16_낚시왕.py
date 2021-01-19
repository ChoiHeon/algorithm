# https://www.acmicpc.net/problem/17143


import heapq

r, c, m = map(int, input().split())
board = [[[] for _ in range(c)] for _ in range(r)]
shark = {}
dir = {1:[-1, 0], 2:[1, 0], 3:[0, 1], 4:[0, -1]}
for k in range(m):
    x, y, s, d, z = map(int, input().split())
    s = (s%(2*r-2)) if d <= 2 else (s%(2*c-2))
    board[x-1][y-1].append(k)
    shark[k] = [[x-1, y-1], s, [*dir[d]], z]

answer = 0
for j in range(c):
    for i in range(r):
        if board[i][j]:
            k = board[i][j].pop()
            answer += shark[k][3]
            del shark[k]
            break

    heap = [[[]for _ in range(c)] for _ in range(r)]
    for k in shark.keys():
        pos, s, dir, z = shark[k][0], shark[k][1], shark[k][2], shark[k][3]
        for _ in range(s):
            if 0 > pos[0]+dir[0] or pos[0]+dir[0] > r-1 or 0 > pos[1]+dir[1] or pos[1]+dir[1] > c-1:
                dir[0], dir[1] = -dir[0], -dir[1]
            pos[0], pos[1] = pos[0]+dir[0], pos[1]+dir[1]
        heapq.heappush(heap[pos[0]][pos[1]], (-z, k))

    for p in range(r):
        for q in range(c):
            if heap[p][q]:
                board[p][q] = [heap[p][q][0][1]]
                for k in heap[p][q][1:]:
                    del shark[k[1]]
            else:
                board[p][q] = []

print(answer)













