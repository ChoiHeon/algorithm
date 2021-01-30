# https://programmers.co.kr/learn/courses/30/lessons/64062


def solution(stones, k):
    left, right = 1, max(stones)
    while left <= right:
        mid = (left + right) // 2
        zero_stone_cnt = 0
        flag = False

        for stone in stones:
            if mid >= stone:
                zero_stone_cnt += 1
            else:
                zero_stone_cnt = 0

            if zero_stone_cnt >= k:
                flag = True
                break

        if flag:
            right = mid - 1
        else:
            left = mid + 1

    return left




print(solution(eval(input()), eval(input())))
