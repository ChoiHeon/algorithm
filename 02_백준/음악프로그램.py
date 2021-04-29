# https://www.acmicpc.net/problem/2623


from collections import defaultdict, deque

n, m = map(int, input().split())
next = defaultdict(set)
prev = defaultdict(set)
queue = deque()
answer = []

for _ in range(m):
    s = [*map(int, input().split())]
    for i in range(1, len(s)-1):
        next[s[i]].add(s[i+1])
        prev[s[i+1]].add(s[i])

for v in range(1, n+1):
    if not prev[v]:
        queue.append(v)

while queue:
    v = queue.popleft()
    answer.append(v)
    for u in next[v]:
        prev[u].remove(v)
        if not prev[u]:
            queue.append(u)


if len(answer) == n:
    for v in answer:
        print(v)
else:
    print(0)