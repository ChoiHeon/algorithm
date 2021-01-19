# https://programmers.co.kr/learn/courses/30/lessons/1843


def solution(arr):
    n= (len(arr) - 1) // 2 + 1
    op = [arr[i * 2 + 1] for i in range(n - 1)]
    dp_max = [[float('-inf')] * n for _ in range(n)]
    dp_min = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        dp_max[i][i] = dp_min[i][i] = int(arr[i*2])

    for k in range(1, n):
        for i in range(0, n - k):
            j = i + k
            for m in range(i, j):
                if op[m] == '+':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][m] + dp_max[m + 1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][m] + dp_max[m + 1][j])
                else:
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][m] - dp_min[m + 1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][m] - dp_max[m + 1][j])

    return dp_max[0][n-1]


print(solution(eval(input())))
