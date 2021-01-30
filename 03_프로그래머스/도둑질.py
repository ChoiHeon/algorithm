# https://programmers.co.kr/learn/courses/30/lessons/42897


def solution(money):
    n = len(money)
    answer = -1

    # 첫 번째 집을 포함 O, 마지막 집을 포함 X
    dp = [0] * (n+1)
    for i in range(n-1):
        dp[i+2] = max(dp[i+2], dp[i]+money[i])  # 선택한 경우
        dp[i+1] = max(dp[i+1], dp[i])           # 선택하지 않는 경우
    answer = max(dp[n-1], dp[n])

    # 첫 번째 집을 포함 X, 마지막 집을 포함 O
    dp = [0] * (n+2)
    for i in range(1, n):
        dp[i+2] = max(dp[i+2], dp[i]+money[i])  # 선택한 경우
        dp[i+1] = max(dp[i+1], dp[i])           # 선택하지 않는 경우
    answer = max(answer, dp[n], dp[n+1])

    return answer


print(solution(eval(input())))
