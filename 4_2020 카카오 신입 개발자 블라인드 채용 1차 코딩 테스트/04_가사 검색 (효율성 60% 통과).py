# https://programmers.co.kr/learn/courses/30/lessons/60060



def match(exp, word):
    n = len(exp)
    if n != len(word):
        return False
    flag = exp[0] == '?'
    s, e, step = (n-1, -1, -1) if flag else (0, n, 1)
    for i in range(s, e, step):
        if exp[i] == '?':
            break
        if exp[i] != word[i]:
            return False
    return True


def solution(words, queries):
    d1 = dict()     # query index
    d2 = dict()     # word matched query count
    s = set(queries)
    n = len(queries)
    answer = [0] * n

    for e in s:
        d1[e] = []
        d2[e] = 0

    for i in range(n):
        d1[queries[i]].append(i)

    for word in words:
        for e in s:
            if match(e, word):
                d2[e] += 1

    for e in s:
        for i in d1[e]:
            answer[i] = d2[e]

    return answer


#print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
print(solution(["kakao"], ["?????"]))