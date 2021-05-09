# https://www.acmicpc.net/problem/1006


"""
원형으로 이어지는 리스트가 문제로 나왔을 떄,
선형으로 계산한 뒤, 원형 조건을 추가해서 해결
"""



import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, w = map(int, input().split())
    area = [[*map(int, input().split())] for _ in range(2)]

    if n == 1:
        print(1 if area[0][0]+area[1][0] <= w else 2)
        continue

    a = [float('inf')]*(n+1)   # 1행 i-1열 & 2행 i-1열까지 전부 채웠을 때 최소 값
    b = [float('inf')]*n       # 1행 i-1열 & 2행 i열까지 전부 채웠을 떄 최소 값
    c = [float('inf')]*n       # 1행 i열 & 2행 i-1열까지 전부 채웠을 때 최소 값

    def solve(s):
        # 점화식
        for i in range(s, n):
            a[i+1] = min(b[i]+1, c[i]+1)
            if area[0][i]+area[1][i] <= w:
                a[i+1] = min(a[i+1], a[i]+1)
            if i > 0 and area[0][i-1]+area[0][i] <= w and area[1][i-1]+area[1][i] <= w:
                a[i+1] = min(a[i+1], a[i-1]+2)

            if i == n-1:
                continue

            b[i+1] = a[i+1]+1
            if area[0][i]+area[0][i+1] <= w:
                b[i+1] = min(b[i+1], c[i]+1)

            c[i+1] = a[i+1]+1
            if area[1][i]+area[1][i+1] <= w:
                c[i+1] = min(c[i+1], b[i]+1)


    a[0], b[0], c[0] = 0, 1, 1
    solve(0)
    answer = a[n]

    f1, f2 = area[0][0]+area[0][-1] <= w, area[1][0]+area[1][-1] <= w

    if f1:
        a[1], b[1], c[1] = 1, 2, 1 if area[1][0]+area[1][1] <= w else 2
        solve(1)
        answer = min(answer, c[n-1]+1)

    if f2:
        a[1], b[1], c[1] = 1, 1 if area[0][0]+area[0][1] <= w else 2, 2
        solve(1)
        answer = min(answer, b[n-1]+1)

    if f1 and f2:
        a[1], b[1], c[1] = 0, 1, 1
        solve(1)
        answer = min(answer, a[n-1]+2)

    print(answer)

