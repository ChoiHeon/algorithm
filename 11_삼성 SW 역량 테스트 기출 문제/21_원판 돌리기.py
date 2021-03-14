# https://www.acmicpc.net/problem/17822


n, m, t = map(int, input().split())
rounds = [[*map(int, input().split())] for _ in range(n)]
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(t):
    x, d, k = map(int, input().split())
    k = k if d else (m - k)  # 역방향 이동 k는 정방향 이동 (m-k)와 동일
    flag = False  # 인접하고 동일한 값들의 존재 여부

    for y in range(x, n+1, x):
        y -= 1  # 인덱스가 0부터 시작하기 때문에 1 감소
        rounds[y] = rounds[y][k:] + rounds[y][:k]

    for i in range(n):
        for j in range(m):
            if rounds[i][j] == 0:
                continue

            # 인접하고 동일한 값을 가진 원소들을 DFS로 탐색
            stack = [(i, j)]
            visited = set()
            while stack:
                a, b = stack.pop()
                visited.add((a, b))
                for dx, dy in dirs:
                    c, d = a + dx, (b + dy) % m
                    if c < 0 or c >= n:
                        continue
                    if rounds[c][d] == rounds[i][j] and (c, d) not in visited:
                        stack.append((c, d))
            if len(visited) > 1:
                flag = True
                for a, b in visited:
                    rounds[a][b] = 0

    # 인접하고 동일한 값들이 존재하지 않을 경우
    if not flag:
        cnt = 0
        avg = 0
        for i in range(n):
            for j in range(m):
                cnt += (rounds[i][j] != 0)
                avg += rounds[i][j]

        # 값이 0 인 원소의 개수가 0개가 아닐 경우
        if cnt != 0:
            avg /= cnt
            for i in range(n):
                for j in range(m):
                    if rounds[i][j] == 0:
                        continue
                    if rounds[i][j] > avg:
                        rounds[i][j] -= 1
                    elif rounds[i][j] < avg:
                        rounds[i][j] += 1

answer = 0
for i in range(n):
    for j in range(m):
        answer += rounds[i][j]

print(answer)
