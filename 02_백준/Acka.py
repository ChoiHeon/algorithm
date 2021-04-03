# https://www.acmicpc.net/problem/12996


def solution(s, a, b, c):
    if s > a+b+c:
        return 0

    # f[k] = k!, 0!은 1로 가정
    f = [1] * (s+1)
    for i in range(2, s+1):
        f[i] = i * f[i-1]

    # comb(n, r) = nCr
    def comb(n, r):
        return f[n] // f[r] // f[n-r]

    # dp[k] = 가수가 할당되지 않은 곡이 k개 이상인 경우의 수, k < s
    # dp[i] = ((jCa * jCb * jCc) * sCj) - dp[i+1], j = s-i
    dp = [0] * (s+1)
    for i in range(s-max(a, b, c), 0, -1):
        j = s-i
        dp[i] += comb(j, a)
        dp[i] *= comb(j, b)
        dp[i] *= comb(j, c)
        dp[i] *= comb(s, j)
        dp[i] -= dp[i+1]

    # 해 = (가수가 배정될 수 있는 모든 경우의 수)
    #      - (가수가 할당되지 않은 곡이 1개 이상인 경우의 수)
    answer = comb(s, a) * comb(s, b) * comb(s, c)
    answer -= dp[1]
    return answer % 1000000007


print(solution(*map(int, input().split())))