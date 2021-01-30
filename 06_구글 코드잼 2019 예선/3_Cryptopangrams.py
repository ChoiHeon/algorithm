# coding=utf-8
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/000000000008830b


def solution():
    N, L = map(int, input().split())
    values = list(map(int, input().split()))
    message = [[] for _ in range(L+1)]

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    prime_set = set()
    for i in range(L-1):
        if values[i] == values[i+1]:
            continue
        prime = gcd(values[i], values[i+1])
        prime_set.add(prime)
        prime_set.add(values[i] // prime)
        prime_set.add(values[i+1] // prime)
        if len(prime_set) == 26:
            break

    prime_lst = sorted(prime_set)
    prime_idx = dict()
    for i in range(26):
        prime_idx[prime_lst[i]] = chr(ord('A') + i)

    for prime in prime_lst:
        answer = [prime_idx[prime]]
        for i in range(L):
            if values[i] % prime != 0:
                break
            prime = values[i] // prime
            answer.append(prime_idx[prime])
        else:
            return "".join(answer)
    return ""


for case in range(1, int(input()) + 1):
    print("Case #{}: {}".format(case, solution()))

