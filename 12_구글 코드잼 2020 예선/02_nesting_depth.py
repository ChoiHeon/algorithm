# 구글 코드잼 2020 예선

for case in range(1, int(input())+1):
    answer = []
    stack = []
    s = list(map(int, input()))

    answer += (['('] * s[0] + [s[0]])
    stack += [')'] * s[0]

    for i in range(1, len(s)):
        if s[i] > s[i-1]:
            answer += ['('] * (s[i] - s[i-1])
            stack += [')'] * (s[i] - s[i-1])
        elif s[i] < s[i-1]:
            for _ in range(s[i-1] - s[i]):
                answer += [stack.pop()]
        answer += [s[i]]
    answer += stack

    print("Case #{}: ".format(case) + "".join(map(str, answer)))

