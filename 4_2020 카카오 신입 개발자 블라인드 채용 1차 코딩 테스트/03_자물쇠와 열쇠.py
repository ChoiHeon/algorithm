# https://programmers.co.kr/learn/courses/30/lessons/60059


def solution(key, lock):
    m, n = len(key), len(lock)
    t = m-1
    k = [[[-1] * m for _ in range(m)] for _ in range(4)]
    l = [[-1] * (n + 2 * t) for __ in range(n + 2 * t)]
    valid = 0

    for i in range(m):
        for j in range(m):
            p, q = i, j
            for r in range(4):
                k[r][i][j] = key[p][q]
                p, q = q, m - p - 1

    for i in range(n):
        for j in range(n):
            l[t+i][t+j] = lock[i][j]
            valid += 1 if lock[i][j] == 0 else 0

    for i in range(n + 2 * t - m+1):
        for j in range(n + 2 * t - m+1):
            for s in range(4):
                flag = False
                cnt = 0
                for x in range(i, i + m):
                    if flag:
                        break
                    for y in range(j, j + m):
                        if k[s][x-i][y-j] == 1:
                            if l[x][y] == 1:
                                flag = True
                                break
                            elif l[x][y] == 0:
                                cnt += 1
                if not flag and cnt == valid:
                    return True
    return False