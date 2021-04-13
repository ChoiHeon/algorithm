# https://www.acmicpc.net/problem/1016


# n 이하의 소수를 배열로 반환하는 함수
def prime(n):
    if n < 2:
        return []
    n += 1
    save = [1] * (n // 2)  # save[i] = 1 if 'Is (2*i+1) prime?' else 0
    for i in range(3, int(n ** 0.5) + 1, 2):
        if save[i // 2]:
            k = i * i
            save[k // 2::i] = [0] * ((n - k - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if save[i]]


# Solution
a, b = map(int, input().split())
sqr = [k**2 for k in range(2, int(b**0.5)+1)]
valid = [1] * (b-a+1)

for m in prime(int(b**0.5)+1):
    n = m**2
    i = a if a%n == 0 else (a//n+1)*n
    for j in range(i-a, b-a+1, n):
        valid[j] = 0

print(sum(valid))
