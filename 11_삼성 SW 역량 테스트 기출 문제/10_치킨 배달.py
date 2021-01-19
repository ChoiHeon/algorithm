# https://www.acmicpc.net/problem/15686

from itertools import combinations


n, m = map(int, input().split())
answer = float('inf')
pubs = []
dists = {}
board = [[*map(int, input().split())] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            if (i, j) not in dists.keys():
                dists[(i, j)] = {}
        elif board[i][j] == 2:
            pubs.append((i, j,))

for house in dists.keys():
    for pub in pubs:
        dists[house][pub] = abs(house[0]-pub[0]) + abs(house[1]-pub[1])

for k in range(1, m+1):
    for sub_pubs in combinations(pubs, k):
        dist = 0
        for house in dists.keys():
            dist += min([dists[house][pub] for pub in sub_pubs])
        answer = min(answer, dist)

print(answer)



