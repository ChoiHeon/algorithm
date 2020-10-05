# https://www.acmicpc.net/workbook/view/1152
# https://www.acmicpc.net/problem/15685

"""
특정점(a)을 기준으로 타겟(b)을 R만큼 회전
    - b를 (-a) 이동
    - b를 회전배열을 이용해 회전
    - b를 a 이동

"""

curves = [[[(0, 0), (0, 1)]],
          [[(0, 0), (-1, 0)]],
          [[(0, 0), (0, -1)]],
          [[(0, 0), (1, 0)]]]

for _ in range(10):
    for i in range(4):
        curves[i].append([])
        for t in curves[i][-2]:
            curves[i][-1].append(t)
        e = curves[i][-1][-1]
        for t in reversed(curves[i][-2][:-1]):
            curves[i][-1].append((t[1]-e[1]+e[0], -t[0]+e[0]+e[1],))

board = [[0]*101 for _ in range(101)]
for _ in range(int(input())):
    x, y, d, g = map(int, input().split())
    for pos in curves[d][g]:
        board[pos[0]+y][pos[1]+x] = 1

answer = 0
for i in range(100):
    for j in range(100):
        if board[i][j] + board[i+1][j] + board[i][j+1] + board[i+1][j+1] == 4:
            answer += 1

print(answer)










