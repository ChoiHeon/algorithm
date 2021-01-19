# https://programmers.co.kr/learn/courses/30/lessons/12920


def solution(n, cores):
    high = n * min(cores)
    low = n // len(cores) * min(cores)
    mid = (high + low) // 2
    while low < high:
        cnt = avail = 0
        for core in cores:
            cnt += mid // core + 1
            if mid % core == 0:
                cnt -= 1
                avail += 1
        if cnt >= n:
            high = mid
        elif cnt + avail < n:
            low = mid+1
        else:
            for i in range(len(cores)):
                if mid % cores[i] == 0:
                    cnt += 1
                if cnt == n:
                    return i + 1
        mid = (high + low) // 2
    return 0


print(solution(eval(input()), eval(input())))
