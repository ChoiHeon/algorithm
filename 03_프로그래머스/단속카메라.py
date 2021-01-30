# https://programmers.co.kr/learn/courses/30/lessons/42884


def solution(routes):
    routes.sort(key=lambda e: e[1])

    answer = 0
    camera = -30001
    for route in routes:
        if camera < route[0]:
            camera = route[1]
            answer += 1

    return answer


print(solution(eval(input())))