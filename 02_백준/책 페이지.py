# https://www.acmicpc.net/problem/1019
# 참고: https://pacific-ocean.tistory.com/240


"""
ex)
    n = 4672 일 때, 4669까지 0~9가 (466+1)*1번 반복됩니다. (0은 1만큼 차감시킵니다)
    일의 자리의 숫자는 모두 계산했으므로 n을 10으로 나눈 뒤, 나머지를 버립니다. (n //= 10)
    이후 n의 값은 466이며 앞의 과정을 n이 10 미만이 될 때까지 반복합니다.
"""


def solution(n):
    a = [0]*10
    b = 1
    while n != 0:
        while n%10 != 9:
            for i in str(n):
                a[int(i)] += b
            n -= 1
        if n < 10:
            for k in range(n+1):
                a[k] += b
            a[0] -= b
            break
        else:
            for i in range(10):
                a[i] += (n//10+1)*b
            a[0] -= b
            b *= 10
            n //= 10

    return ' '.join(map(str, a))


print(solution(int(input())))