# https://www.acmicpc.net/problem/16235


import sys

read = sys.stdin.readline
n, m, t = map(int, read().split())
food = [[5]*n for _ in range(n)]
robot = [list(map(int, read().split())) for _ in range(n)]
trees = [[[] for _ in range(n)] for _ in range(n)]
around = {(i, j): [] for i in range(n) for j in range(n)}

for i, j in around.keys():
    for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        if -1 < i+dx < n and -1 < j+dy < n:
            around[i, j].append((i+dx, j+dy,))

for _ in range(m):
    x, y, z = map(int, read().split())
    trees[x-1][y-1].append(z)

for _ in range(t):
    for i in range(n):
        for j in range(n):
            for k in range(len(trees[i][j])):
                if food[i][j] < trees[i][j][k]:
                    food[i][j] += sum(map(lambda e: e//2, trees[i][j][k:]))
                    trees[i][j] = trees[i][j][:k]
                    break
                else:
                    food[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
    for i in range(n):
        for j in range(n):
            for tree in trees[i][j]:
                if tree%5 == 0:
                    for x, y in around[i, j]:
                        trees[x][y].insert(0, 1)
            food[i][j] += robot[i][j]

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])

print(answer)





