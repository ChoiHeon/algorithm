# main
# https://www.acmicpc.net/problem/1904

N = int(input())

if N < 3:
    print(N)
else:
    alpha = 1
    beta = 2
    for _ in range(N - 2):
        temp = beta
        beta = (beta + alpha) % 15746
        alpha = temp
    print(beta)


