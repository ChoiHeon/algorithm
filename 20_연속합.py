# https://www.acmicpc.net/problem/1912

n = int(input())
p = list(map(int, input().split()))

for i in range(1, n):
    if p[i-1] > 0:
        p[i] += p[i-1]

print(max(p))
        