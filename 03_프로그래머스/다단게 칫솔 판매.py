# https://programmers.co.kr/learn/courses/30/lessons/77486


def solution(enroll, referral, seller, amount):
    n = len(enroll)
    id = {enroll[i]:i+1 for i in range(n)}
    id['-'] = 0

    r_id = [0]*(n+1)
    for i in range(n):
        r_id[i+1] = id[referral[i]]

    answer = [0]*(n+1)
    for i in range(len(seller)):
        s, m = id[seller[i]], amount[i]*100
        while s != 0 or m != 0:
            answer[s] += (m-int(m/10))
            s = r_id[s]
            m = int(m/10)

    return answer[1:]


# test
print(solution(eval(input()), eval(input()), eval(input()), eval(input())))