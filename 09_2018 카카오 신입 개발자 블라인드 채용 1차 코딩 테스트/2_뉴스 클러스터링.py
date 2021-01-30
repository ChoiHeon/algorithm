# https://programmers.co.kr/learn/courses/30/lessons/17677


def solution(str1, str2):
    from collections import Counter

    def multiset(s):
        ret = []
        for i in range(len(s)-1):
            e = s[i:i+2]
            if str(e).isalpha():
                ret.append(e)
        return ret

    A = Counter(multiset(str1.upper()))
    B = Counter(multiset(str2.upper()))
    I = A.keys() & B.keys()
    U = A.keys() | B.keys()
    n1 = sum(map(lambda e: min(A[e], B[e]), I))
    n2 = sum(map(lambda e: max(A[e], B[e]), U))

    return (int)(((n1 / n2) if len(U) != 0 else 1) * 65536)


print(solution(eval(input()), eval(input())))
