# https://programmers.co.kr/learn/courses/30/lessons/12971


def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    def max_value(sub):
        dp = [[0, 0] for _ in range(len(sub))]
        dp[0][1] = sub[0]

        for i in range(2, len(sub)):
            dp[i][0] = max(dp[i-1])
            dp[i][1] = dp[i-1][0] + sub[i]

        return max(dp[-1])

    return max(max_value(sticker[:-1]), max_value(sticker[1:]))


# testS
print(solution(eval(input())))