# https://programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    from collections import deque

    msg = deque(msg)
    answer = []

    d = dict()
    for i in range(26):
        d[chr(i+ord('A'))] = i+1

    v = 27
    while msg:
        w = ""
        for i in range(len(msg)):
            w += msg.popleft()
            if w not in d.keys():
                d[w] = v
                v += 1
                msg.appendleft(w[-1])
                w = w[:-1]
                break
        answer.append(d[w])
    return answer





print(solution(eval(input())))
