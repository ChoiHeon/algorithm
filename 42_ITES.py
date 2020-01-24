# https://www.algospot.com/judge/problem/read/ITES

# 문제 해석을 잘못함
# 풀이 도중 파이썬으로는 해결하기 어렵다는 것을 알게됨
KEY = 2**32
A = [1983]
for r in [0] * int(input()):
    K, N = map(int, input().split())
    if N > len(A):
        for _ in range(N-len(A)):
            A.append((A[-1] * 214013 + 2531011) % KEY)
    S = list(map(int, str(A[N-1]%10000+1))); L = len(S); P = [[i, int(S[i])] for i in range(len(S))]
    while P:
        t = P.pop()
        if t[1] == K:
            r += 1
        elif t[0] < L-1:
            P += [t[0]+1, t[1] + S[t[0]+1]],
    print(r)

