# https://www.acmicpc.net/problem/2166


n = int(input())
p = [[*map(int, input().split())] for _ in range(n)]
a = 0

for i in range(-1, n-1):
    a += ((p[i][0]*p[i+1][1]/2)-p[i+1][0]*p[i][1]/2)

print('%.1f'%(abs(a)))
