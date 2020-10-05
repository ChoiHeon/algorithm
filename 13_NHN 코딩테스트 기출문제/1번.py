
n = int(input())
board = [[*map(int, input().split())] for _ in range(n)]
visited = set()
answer = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and (i, j,) not in visited:
            stack = [(i, j,)]
            area = {(i, j,)}
            while stack:
                x, y = stack.pop()
                for p, q in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    if x+p < 0 or x+p > n-1 or y+q < 0 or y+q > n-1 \
                            or board[x+p][y+q] == 0 or (x+p, y+q,) in area:
                        continue
                    area.add((x+p, y+q,))
                    stack.append((x+p, y+q,))
            visited.update(area)
            answer.append(len(area))

print(len(answer))
print(' '.join(map(str, sorted(answer)))) if answer else None
