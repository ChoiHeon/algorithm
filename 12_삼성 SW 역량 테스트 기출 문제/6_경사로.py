# https://www.acmicpc.net/workbook/view/1152
# https://www.acmicpc.net/problem/14890

N, L = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(N)]


def solution(line):
    dists = [[0, 0, line[0], 1]]  # start, end, value, length
    check = [1] * N

    for i in range(1, N):
        if dists[-1][2] == line[i]: dists[-1][1], dists[-1][3] = i, dists[-1][3]+1
        else:                       dists.append([i, i, line[i], 1])

    for i in range(len(dists)-1):
        if abs(dists[i][2] - dists[i+1][2]) > 1:
            return 0
        if dists[i][2] < dists[i+1][2]:
            if dists[i][3] < L:
                return 0
            for j in range(dists[i][1], dists[i][1]-L, -1):
                if check[j] == 0:
                    return 0
                check[j] = 0
        else:
            if dists[i+1][3] < L:
                return 0
            for j in range(dists[i+1][0], dists[i+1][0]+L):
                if check[j] == 0:
                    return 0
                check[j] = 0

    return 1


answer = 0
for line in board:
    answer += solution(line)
for line in zip(*board):
    answer += solution(line)

print(answer)



