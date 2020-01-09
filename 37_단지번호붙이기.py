# https://www.acmicpc.net/problem/2667

w = []


def f(n, i, j):
    global w
    if 0 <= i < n and 0 <= j < n and w[i][j]:
        w[i][j] = 0
        return 1 + f(n, i+1, j) + f(n, i-1, j) + f(n, i, j+1) + f(n, i, j-1)
    return 0


n = int(input())
for _ in range(n):
    w.append(list(map(int, input())))

answer = []
for i in range(n):
    for j in range(n):
        if w[i][j]:
            answer.append(f(n, i, j))
answer.sort()

print(len(answer))
for c in answer:
    print(c)

'''
숏코딩
출처: https://www.acmicpc.net/source/5517483
r,d,*a=0,{(x,y)for y in range(int(input()))for x,c in enumerate(input())if'0'<c}
while d:
    s=[d.pop()];r+=1;b=0
    while s:
        x,y=s.pop();b+=1
        for e in-2,0,2,4:
            p=x+e//3,y+e%3-1
            if{p}<=d:d-={p};s+=p,
    a+=b,
print(*[r]+sorted(a))
'''
