# https://www.acmicpc.net/problem/2239


import sys
sys.setrecursionlimit(10**6)

board = [[*map(int, input())] for _ in range(9)]
row = [{*range(1, 10)} for _ in range(9)]
col = [{*range(1, 10)} for _ in range(9)]
area = [{*range(1, 10)} for _ in range(9)]
blank = []

for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            row[i].remove(board[i][j])
            col[j].remove(board[i][j])
            area[(i//3)*3+(j//3)].remove(board[i][j])
        else:
            blank.append((i, j))


def sudoku(k):
    global row, col, area
    if k == len(blank):
        return True

    x, y = blank[k]
    z = (x//3)*3+(y//3)
    s = row[x].intersection(col[y]).intersection(area[z])

    for i in sorted(s):
        board[x][y] = i
        row[x].remove(i); col[y].remove(i); area[z].remove(i)
        if sudoku(k+1):
            return True
        row[x].add(i); col[y].add(i); area[z].add(i)

    return False


sudoku(0)
for i in range(9):
    for j in range(9):
        print(board[i][j], end='')
    print()