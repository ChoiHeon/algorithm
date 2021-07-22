# https://www.acmicpc.net/problem/9466


import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = [0] + [*map(int, input().split())]
    visited = [False] * (n+1)
    answer = 0

    for i in range(1, n+1):
        x = i
        while not visited[x]:
            visited[x] = True
            x = s[x]
        y = i
        while x != y:
            answer += 1
            y = s[y]

    print(answer)



