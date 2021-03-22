# https://www.acmicpc.net/problem/2023


from collections import deque

n = int(input())
answer = deque([2, 3, 5, 7])
for i in range(1, n):
    for _ in range(len(answer)):
        p = answer.popleft()
        for i in range(1, 10, 2):
            q = 10*p + i
            for j in range(3, int(q**0.5)+1, 2):
                if q % j == 0:
                    break
            else:
                answer.append(q)
for p in answer:
    print(p)