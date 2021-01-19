# https://www.acmicpc.net/problem/16236


from collections import deque
import heapq


n = int(input())
board = [list(map(int, input().split()))for _ in range(n)]
shark_size, shark_eat = 2, 0
shark_pos = (-1, -1)
answer = 0

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            shark_pos = (i, j)
            board[i][j] = 0

while True:
    stack = deque([shark_pos])
    visited = {shark_pos}
    dist = -1
    target = []
    while stack:
        for _ in range(len(stack)):
            pos = stack.popleft()
            if 0 < board[pos[0]][pos[1]] < shark_size:
                heapq.heappush(target, pos)
            if pos[0] > 0 and (pos[0]-1, pos[1]) not in visited and board[pos[0]-1][pos[1]] <= shark_size:
                stack.append((pos[0]-1, pos[1])); visited.add((pos[0]-1, pos[1]))
            if pos[1] > 0 and (pos[0], pos[1]-1) not in visited and board[pos[0]][pos[1]-1] <= shark_size:
                stack.append((pos[0], pos[1]-1)); visited.add((pos[0], pos[1]-1))
            if pos[1] < n-1 and (pos[0], pos[1]+1) not in visited and board[pos[0]][pos[1]+1] <= shark_size:
                stack.append((pos[0], pos[1]+1)); visited.add((pos[0], pos[1]+1))
            if pos[0] < n-1 and (pos[0]+1, pos[1]) not in visited and board[pos[0]+1][pos[1]] <= shark_size:
                stack.append((pos[0]+1, pos[1])); visited.add((pos[0]+1, pos[1]))
        dist += 1
        if target:
            break
    else:
        break

    pos = target[0]
    board[pos[0]][pos[1]] = 0
    shark_pos = pos
    answer += dist
    shark_eat += 1
    if shark_eat == shark_size:
        shark_size += 1
        shark_eat = 0

print(answer)









