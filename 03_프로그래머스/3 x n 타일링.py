# https://programmers.co.kr/learn/courses/30/lessons/12902


def solution(n):
    if n%2 != 0:
        return 0

    dp = [0] * 5010
    dp[0], dp[2] = 1, 3

    # 점화식
    # dp[k] = dp[k-2]*dp[2] + dp[k-4]*2 + dp[k-6]*2 + ... + dp[0]*2 (k >= 4)
    for i in range(4, n+1, 2):
        dp[i] += dp[i-2] * dp[2]
        for j in range(i-4, -1, -2):
            dp[i] += dp[j] * 2          # 2 =  (i-j)칸에서만 생성가능한 고유한 모양의 가짓수

    return dp[n] % 1000000007

print(solution(eval(input())))
