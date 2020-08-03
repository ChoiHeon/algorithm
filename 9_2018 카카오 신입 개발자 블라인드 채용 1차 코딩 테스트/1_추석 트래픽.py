# https://programmers.co.kr/learn/courses/30/lessons/17676


def solution(lines):
    times = []
    bounds = []
    answer = 0

    for line in lines:
        _, e, t = line.split()

        e = map(float, e.split(':'))
        e = sum(map(lambda e: 60 ** e[0] * e[1] * 1000, zip(range(2, -1, -1), e)))
        t = flaot(t[:-1]) * 1000
        s = e - t + 1
        times.append((s,e, ))

    for time in times:
        bounds.append((time[0], time[0] + 999,))
        bounds.append((time[0] - 999, time[0],))
        bounds.append((time[1] - 999, time[1],))
        bounds.append((time[1], time[1] + 999,))

    for bound in bounds:
        cnt = 0
        for time in times:
            if bound[0] > time[1] or bound[1] < time[0]:
                continue
            cnt += 1
        answer = max(answer , cnt)

    return answer


print(solution(eval(input())))
