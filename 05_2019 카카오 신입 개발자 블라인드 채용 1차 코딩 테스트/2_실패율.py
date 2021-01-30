# https://programmers.co.kr/learn/courses/30/lessons/42889

"""
    stage는 최대 200000, N은 최대 500이므로
    N을 기준으로 반복문을 할 경우 더 빠름

"""

def solution(N, stages):
    log = [[0, 0] for _ in range(N+1)]    #[0] / [1] = failure rate

    for stage in stages:
        log[stage-1][0] += 1
        for i in range(stage):
            log[i][1] += 1

    rates = list(enumerate([log[i][0] / log[i][1] if log[i][1] != 0 else 0 for i in range(N)]))
    rates.sort(key=lambda e: (-e[1], e[0]))
    return [rates[i][0]+1 for i in range(N)]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))


