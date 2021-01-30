# https://programmers.co.kr/learn/courses/30/lessons/17678


def solution(n, t, m, timetable):
    crew_times = sorted([*map(lambda e: [*map(int, e.split(':'))], timetable)])
    bus_times = [(9 + (t*i)//60, (t*i)%60) if t*i >= 60 else (9, t*i, ) for i in range(n)]

    schedule = dict()
    for bus in bus_times:
        schedule[bus] = []

    waiting = True
    for bus in bus_times:
        if not waiting:
            break
        for _ in range(m):
            if not crew_times:
                waiting = False
                break
            crew = crew_times[0]
            if bus[0] == crew[0] and bus[1] < crew[1]  or bus[0] < crew[0]:
                break
            schedule[bus].append(crew_times.pop(0))

    if len(schedule[bus_times[-1]]) < m:
        answer = bus_times[-1]
    else:
        answer = schedule[bus_times[-1]][-1]
        if answer[1] == 0:
            answer[0], answer[1] = answer[0]-1, 59
        else:
            answer[1] -= 1

    answer = map(lambda e: str(e).zfill(2), answer)
    return ':'.join(answer)


print(solution(eval(input()), eval(input()), eval(input()), eval(input())))
