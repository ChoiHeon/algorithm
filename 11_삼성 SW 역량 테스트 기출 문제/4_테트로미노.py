# https://www.acmicpc.net/problem/14500


blocks = [[[(0, 0), (0, 1), (0, 2), (0, 3)], 1, 4], [[(0, 0), (0, 1), (1, 0), (1, 1)], 2, 2],
          [[(0, 0), (1, 0), (2, 0), (2, 1)], 3, 2], [[(0, 0), (1, 0), (1, 1), (2, 1)], 3, 2],
          [[(0, 0), (0, 1), (1, 1), (0, 2)], 2, 3]]

n, m = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(n)]
answer = 0

def func():
    global answer
    for _ in range(4):
        for block in blocks:
            h, w = block[1], block[2]
            for i in range(n-h+1):
                for j in range(m-w+1):
                    answer = max(answer, sum(map(lambda e: board[e[0]+i][e[1]+j], block[0])))
            block[0] = [*map(lambda e: (e[1], (block[1]-e[0]-1),), block[0])]
            block[1], block[2] = block[2], block[1]

func()

for block in blocks:
    block[0] = [*map(lambda e: (block[1]-e[0]-1, e[1],), block[0])]

func()

print(answer)


