# https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3


def f(n):
    if n == 0:
        return 0
    return 1 + f(n//10)


def solution(s):
    n = len(s)
    answer = n

    for i in range(1, n//2 + 1):
        p = []  # sub word
        q = []  # count
        for j in range(0, n, i):
            if p:
                if p[-1] == s[j:j + i]:
                    q[-1] = q[-1] + 1
                else:
                    p.append(s[j:j + i])
                    q.append(1)
            else:
                p.append(s[j:j + i])
                q.append(1)

        temp = len(p) * i if n % i == 0 else (len(p)-1) * i + n % i
        temp += sum(map(lambda e: 0 if e == 1 else f(e), q))
        answer = min(answer, temp)
    return answer


print(solution(input()))
