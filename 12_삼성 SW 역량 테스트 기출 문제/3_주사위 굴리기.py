# https://www.acmicpc.net/problem/14499


"""
    * 주사위 정보를 x, y, z축으로 나눠서 저장
"""



n, m, y, x, k = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(n)]
dir = {'1':(0, 1), '2':(0, -1), '3':(-1, 0), '4':(1, 0)}
dice_x, dice_y, dice_z = [0, 0], [0, 0], [0, 0]

for cmd in input().split():
    next_y, next_x = y + dir[cmd][0], x + dir[cmd][1]
    if next_x < 0 or next_x > m-1 or next_y < 0 or next_y > n-1:
        continue

    if cmd == '1':
        dice_x[0], dice_x[1], dice_z[0], dice_z[1] =\
        dice_z[0], dice_z[1], dice_x[1], dice_x[0]
    elif cmd == '2':
        dice_x[0], dice_x[1], dice_z[0], dice_z[1] =\
        dice_z[1], dice_z[0], dice_x[0], dice_x[1]
    elif cmd == '3':
        dice_y[0], dice_y[1], dice_z[0], dice_z[1] =\
        dice_z[1], dice_z[0], dice_y[0], dice_y[1]
    elif cmd == '4':
        dice_y[0], dice_y[1], dice_z[0], dice_z[1] =\
        dice_z[0], dice_z[1], dice_y[1], dice_y[0]

    y, x = next_y, next_x
    if board[y][x] == 0:    board[y][x] = dice_z[0]
    else:                   dice_z[0], board[y][x] = board[y][x], 0

    print(dice_z[1])

