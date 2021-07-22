# https://www.acmicpc.net/problem/1920

n = int(input())
p = sorted(list(map(int, input().split())))
input()
for x in map(int, input().split()):
    r, h = 0, n-1
    ans = 0
    while r <= h:
        m = (r+h)//2
        if p[m] == x:
            ans = 1
            break
        elif p[m] < x:
            r = m+1
        else:
            h = m-1
    print(ans)