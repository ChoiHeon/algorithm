# https://www.acmicpc.net/problem/17140


from collections import Counter


r, c, k = map(int, input().split())
r, c = r-1, c-1
a = [list(map(int, input().split())) for _ in range(3)]
r_len = c_len = 3


def func(c, n):
    len_list = [0]*n
    for i in range(n):
        cntr = Counter(c[i])
        del cntr[0]
        len_list[i] = len(cntr.keys())*2
        temp = sorted([*cntr.items()], key=lambda e: (e[1], e[0]))
        c[i] = []
        for e in temp:
            c[i].append(e[0]);  c[i].append(e[1])

    max_len = max(len_list)
    for i in range(n):
        c[i] = c[i] + [0]*(max_len-len_list[i])

    if max_len > 100:
        for i in range(n):
            c[i] = c[i][:100]

    return min(max_len, 100)


for t in range(101):
    if r < r_len and c < c_len and a[r][c] == k:
        print(t)
        break

    if r_len < c_len:
        b = [[a[i][j] for i in range(r_len)] for j in range(c_len-1, -1, -1)]
        r_len = func(b, c_len)
        a = [[b[i][j] for i in range(c_len-1, -1, -1)] for j in range(r_len)]
    else:
        c_len = func(a, r_len)
else:
    print(-1)













