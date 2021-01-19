# https://programmers.co.kr/learn/courses/30/lessons/43236


def solution(distance, rocks, n):
    m = len(rocks)
    tmp = sorted(rocks + [0, distance])
    dists = [tmp[i+1]-tmp[i] for i in range(m + 1)]

    answer = -1
    start, end = 0, distance
    while start <= end:
        mid = (start+end)//2
        cnt = 0
        dists_copy = dists.copy()
        for i in range(m):
            if dists_copy[i] <= mid:
                dists_copy[i+1] += dists_copy[i]
                dists_copy[i] = float('inf')
                cnt += 1

        if cnt > n:
            end = mid-1
        else:
            answer = max(answer, min(dists_copy))
            start = mid + 1
    return answer


print(solution(eval(input()), eval(input()), eval(input())))
