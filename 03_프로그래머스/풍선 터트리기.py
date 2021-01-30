# https://programmers.co.kr/learn/courses/30/lessons/68646


def solution(a):
    n = len(a)
    min_left = [0] * n
    min_right = [0] * n
    left = right = float('inf')

    for i in range(n):
        left = min(a[i], left)
        right = min(a[n-i-1], right)

        min_left[i] = left
        min_right[n-i-1] = right

    answer = 0
    for i in range(n):
        if a[i] <= min_left[i] or a[i] <= min_right[i]:
            answer += 1

    return answer

