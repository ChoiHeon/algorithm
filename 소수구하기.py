# https://www.acmicpc.net/problem/1929


def is_prime(num):
    if num == 1:
        return False
    n = int(num ** 0.5)
    for k in range(2, n+1):
        if num % k == 0:
            return False
    return True


M, N = map(int, input().split())
for i in range(M, N+1):
    if is_prime(i):
        print(i)
