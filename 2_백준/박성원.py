# https://www.acmicpc.net/problem/1086


"""
* 모듈러 공식
    - (p + q) % r = ((p % r) + (q % r)) % r
    - (p * q) % r = ((p % r) * (q * r)) % r

* 동적 프로그래밍(DP)
    - dp[i][j] = i는 비트마스크, j는 i에 활성화된 정수들의 합친수들을 k로 나눈 나머지
    - dp[new][nxt] = new는 i에 활성화되지 않은 비트 1개를 활성화 했을 때의 비트마스크
                     l번째 비트를 활성화했을 때
                     nxt = ((j * (10 ** s[l]의길이) % k) % k + s[l] % k) % k
                     --> i로 생성할 수 있는 합친수의 뒤에 s[l]을 붙인다음 k로 나눈 나머지를 의미

    - 위의 식에 대해서  i를 0부터 (1 << n)-1까지 반복하면 전체를 확인할 수 있음
    - i보다 new가 항상 값이 더 크기 때문
"""


import sys, math
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
s = list(set([int(input()) for _ in range(n)]))
k = int(input())

bm = (1 << n) - 1
dp = [[0] * k for _ in range(bm+1)]
ten = [1]     # [1, 10, 100, 1000, ... ]
for _ in range(1, 51):
    ten.append(ten[-1] * 10)
ten_mod = list(map(lambda e: ten[len(str(s[e]))] % k, range(n)))
ele_mod = list(map(lambda e: e % k, s))

dp[0][0] = 1
for i in range(bm):
    for j in range(k):
        for p in range(n):
            if i & (1 << p) == 0:
                new = i | (1 << p)
                nxt = ((j * ten_mod[p]) % k + ele_mod[p]) % k
                dp[new][nxt] += dp[i][j]

num = dp[-1][0]             # 분자
den = math.factorial(n)     # 분모
tmp = math.gcd(den, num)

num = dp[-1][0] // tmp
den = 1 if num == 0 else den // tmp
print("{}/{}".format(num, den))