# https://www.acmicpc.net/problem/17779

n = int(input())
board = [[*map(int, input().split())] for _ in range(n)]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
group_start = [(0, 0, 1), (0, n-1, 2), (n-1, 0, 3), (n-1, n-1, 4)]


def solution(x, y, d1, d2):
    groups = [[0] * n for _ in range(n)]
    people_count = [0] * 5

    # 5번 그룹 경계선
    for i in range(0, d1 + 1):
        groups[x+i][y-i] = 5
        groups[x+d2+i][y+d2-i] = 5
    for i in range(0, d2 + 1):
        groups[x+i][y+i]= 5
        groups[x+d1+i][y-d1+i] = 5

    # 1 ~ 4번 그룹 경계선
    for i in range(x):
        groups[i][y] = 1
    for j in range(y+d2+1, n):
        groups[x+d2][j] = 2
    for j in range(y-d1):
        groups[x+d1][j] = 3
    for i in range(x+d1+d2+1, n):
        groups[i][y-d1+d2] = 4

    def dfs(i, j, group_num):
        if i < 0 or i > n-1 or j < 0 or j > n-1:
            return
        if groups[i][j] == 0:
            groups[i][j] = group_num
            for dx, dy, in dir:
                dfs(i+dx, j+dy, group_num)

    for i, j, group_num in group_start:
        dfs(i, j, group_num)

    for i in range(n):
        for j in range(n):
            if groups[i][j] % 5 == 0:
                people_count[4] += board[i][j]
            else:
                people_count[groups[i][j]-1] += board[i][j]

    return max(people_count) - min(people_count)


answer = float('inf')
for x in range(n-2):
    for d1 in range(1, n):
        for d2 in range(1, n-x-d1):
            for y in range(d1, n-d2):
                answer = min(answer, solution(x, y, d1, d2))

print(answer)