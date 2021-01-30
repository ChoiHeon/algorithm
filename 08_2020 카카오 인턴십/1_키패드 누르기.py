# https://programmers.co.kr/learn/courses/30/lessons/67256


def solution(numbers, hand):
    handed = 0 if hand == 'left' else 1
    hand_pos = [[3, 0], [3, 2]]
    key_pos = [[3, 1]] + [[i//3, i%3] for i in range(9)]
    answer = []

    is_right = -1
    for n in numbers:
        m = n % 3
        if n == 0 or m == 2:
            l_dis = abs(hand_pos[0][0] - key_pos[n][0]) + abs(hand_pos[0][1] - key_pos[n][1])
            r_dis = abs(hand_pos[1][0] - key_pos[n][0]) + abs(hand_pos[1][1] - key_pos[n][1])

            if l_dis == r_dis:
                is_right = handed
            else:
                is_right = 0 if l_dis < r_dis else 1
        else:
            is_right = abs(m-1)

        answer.append('R' if is_right else 'L')
        hand_pos[is_right] = key_pos[n]

    return ''.join(answer)


print(solution(eval(input()), eval(input())))
