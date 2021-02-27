# https://programmers.co.kr/learn/courses/30/lessons/12987


def solution(A, B):
    answer = 0
    n = len(A)
    i = j = 0

    A.sort()
    B.sort()

    while j < n:
        if A[i] < B[j]:
            answer += 1
            i, j = i + 1, j + 1
        else:
            j += 1

    return answer


# test
print(solution(eval(input()), eval(input())))