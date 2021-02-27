# https://programmers.co.kr/learn/courses/30/lessons/12983


def solution(strs, t):
    dp = [0] + [float('inf')]*len(t)
    strs = set(strs)

    for i in range(1, len(t) + 1):
        for k in range(1, 6):
            s = 0 if i < k else (i-k)

            if t[s:i] in strs:
                dp[i] = min(dp[i], dp[i-k] + 1)

    return dp[-1] if dp[-1] != float('inf') else -1


# test
print(solution(eval(input()), eval(input())))