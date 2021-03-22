# https://www.acmicpc.net/problem/20303


n, m, k = map(int, input().split())
child = [*map(int, input().split())]
rel = {i : [] for i in range(n)}
group = []

# 관계 생성
for _ in range(m):
    a, b = map(lambda e: int(e)-1, input().split())
    rel[a].append(b)
    rel[b].append(a)

# 그룹 생성
for i in range(n):
    if child[i] < 0:
        continue
    stack = [i]
    group.append([1, child[i]])  # 그룹의 인원 수, 총 사탕 개수
    child[i] = -1
    while stack:
        a = stack.pop()
        for b in rel[a]:
            if child[b] < 0:
                continue
            group[-1][0] += 1
            group[-1][1] += child[b]
            child[b] = -1
            stack.append(b)

group.sort(key=lambda e: e[0])
dp = [0] * (k)

for count, total in group:
    for i in range(k-1, -1, -1):
        if i < count:
            dp[i] = dp[i]
        else:
            dp[i] = max(dp[i], dp[i-count] + total)

print(dp[-1])
