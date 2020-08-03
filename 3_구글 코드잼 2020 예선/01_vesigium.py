# 구글 코드잼 2020 예선

import sys
input = sys.stdin.readline

for t in range(1, int(input()) + 1):
    n = int(input())
    bm_row = [0] * n
    bm_col = [0] * n
    check_row = [False] * n
    check_col = [False] * n
    trace = 0
    rows = 0
    cols = 0

    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(n):
            if i == j:
                trace += row[j]

            if not check_row[i]:
                if bm_row[i] & (1 << (row[j] - 1)):
                    check_row[i] = True
                    rows += 1
                else:
                    bm_row[i] |= (1 << (row[j] - 1))

            if not check_col[j]:
                if bm_col[j] & (1 << (row[j] - 1)):
                    check_col[j] = True
                    cols += 1
                else:
                    bm_col[j] |= (1 << (row[j] - 1))

    print("Case #{}: {} {} {}".format(t, trace, rows, cols))
