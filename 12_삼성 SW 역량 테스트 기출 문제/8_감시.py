# https://www.acmicpc.net/workbook/view/1152
# https://www.acmicpc.net/problem/15683


from itertools import product


init_dir = [[[(-1, 0)], [(0, 1)], [(1, 0)], [(0, -1)]],
           [[(-1, 0), (1, 0)], [(0, 1), (0, -1)]],
           [[(1, 0), (0, 1)], [(0, 1), (-1, 0)], [(-1, 0), (0, -1)], [(0, -1), (1, 0)]],
           [[(1, 0), (0, 1), (-1, 0)], [(0, 1), (-1, 0), (0, -1)], [(-1, 0), (0, -1), (1, 0)], [(0, -1), (1, 0), (0, 1)]],
           [[(1, 0), (0, 1), (-1, 0), (0, -1)]]]
n, m = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(n)]
cam_pos, cam_dir = [], []
empty, answer = 0, float('inf')

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            empty += 1
        elif board[i][j] < 6:
            cam_pos.append((i, j,))
            cam_dir.append(init_dir[board[i][j]-1])

for dir_info in product(*cam_dir):
    monitor = set()
    for i in range(len(dir_info)):
        for dir in dir_info[i]:
            pos = cam_pos[i]
            while True:
                y, x = pos[0]+dir[0], pos[1]+dir[1]
                if y < 0 or y > n-1 or x < 0 or x > m-1 or board[y][x] == 6:
                    break
                pos = (y, x,)
                if board[y][x] == 0:
                    monitor.add(pos)
    answer = min(answer, empty - len(monitor))

print(answer)





