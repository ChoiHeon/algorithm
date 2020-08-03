# https://programmers.co.kr/learn/courses/30/lessons/60061


"""
* 문제에서 주어진 조건을 잘 파악해야 하는 문제
* 기둥이나 바닥을 삭제할 경우
    - 삭제하고자 하는 위치의 주변이 삭제 가능 조건을 만족하는지 검사 --> 다양한 상황에 맞는 다양한 조건들을 검사해야 함
    - 삭제 가능 여부와 상관없이 삭제 한 후, 주변이 조건을 만족하는지를 검사 --> 조건을 만족하지 않았을 경우, 다시 생성
    - 두 번째 방법이 더 간단하게 조건을 검사할 수 있음
"""


c = []
f = []


def check_column(n, x, y):   # 기둥이 유효한지 검사
    if x < 0 or x > n or y < 0 or y > n-1 or c[x][y] == 0:  # 검사 생략 조건
        return True
    return y == 0 or c[x][y-1] or (0 < x and f[x-1][y]) or f[x][y]


def check_floor(n, x, y):    # 바닥이 유효한지 검사
    if x < 0 or x > n-1 or y < 1 or y > n or f[x][y] == 0:  # 검사 생략 조건
        return True
    return (0 < x and f[x-1][y] and f[x+1][y]) or c[x][y-1] or c[x+1][y-1]


def solution(n, build_frame):
    global c, f
    c = [[0] * (n + 1) for _ in range(n + 1)]
    f = [[0] * (n + 1) for _ in range(n + 1)]

    for x, y, a, b in build_frame:
        if a == 0:          # 기둥
            if b == 1:      # 생성
                c[x][y] = 1
                if not check_column(n, x, y):
                    c[x][y] = 0
            else:           # 삭제
                c[x][y] = 0
                if not (check_column(n, x, y+1) and check_floor(n, x-1, y+1) and check_floor(n, x, y+1)):
                    c[x][y] = 1
        else:               # 바닥
            if b == 1:      # 생성
                f[x][y] = 1
                if not check_floor(n, x, y):
                    f[x][y] = 0
            else:           # 삭제
                f[x][y] = 0
                if not (check_column(n, x, y) and check_column(n, x+1, y) and check_floor(n, x-1, y) and check_floor(n, x+1, y)):
                    f[x][y] = 1

    answer = []
    for i in range(n+1):
        for j in range(n+1):
            if c[i][j]:
                answer.append([i, j, 0])
            if f[i][j]:
                answer.append([i, j, 1])
    return sorted(answer)


input_data = eval(input())
solution(5, input_data)

