# https://programmers.co.kr/learn/courses/30/lessons/12929


"""
* 설명
    N이 주어지면 2 * N개의 자리를 채워야 한다
    첫 번째 자리는 무조건 '('이 와야 하는데
    첫 번째 '('과 매치되는 ')'가 들어갈 수 있는 자리는 정해져있다. (2, 4, ... , N)
    첫 번째 괄호쌍 '()'가 차지한 자리에 외에 들어갈 수 있는 괄호쌍의 개수를 알 수 있으면 쉽게 구할 수 있다.
    (연속된 자리들에는 올바른 괄호들이 들어가야 한다)

* 초기화
    dp[0] = 1
    dp[1] = 1

* 점화식
    dp[k] = dp[0]*dp[k-1] + dp[1]*dp[k-1-1] + ... + dp[i] * dp[k-i-1] + ... + dp[k-1]*dp[0]
"""


def solution(n):
    dp = [0] * (n+1)
    dp[0], dp[1] = 1, 1

    for i in range(2, n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-j-1]

    return dp[n]


# test
print(solution(int(input())))