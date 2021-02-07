# https://programmers.co.kr/learn/courses/30/lessons/72414


def convert2second(time):
    hour, minute, second = map(int, time.split(':'))
    return hour * 3600 + minute * 60 + second


def convert2time(second):
    hour, minute, second = second // 3600, (second % 3600) // 60, second % 60
    return ':'.join(map(lambda e: str(e).zfill(2), [hour, minute, second]))


def solution(play_time, adv_time, logs):
    answer = 0
    play_time = convert2second(play_time)
    adv_time = convert2second(adv_time)
    logs = [*map(lambda log: [*map(convert2second, log.split('-'))], logs)]
    total_times = [0] * (play_time + 1)
    max_time = 0

    for log in logs:
        total_times[log[0]] += 1
        total_times[log[1]] -= 1

    for i in range(1, play_time):
        total_times[i] += total_times[i - 1]

    # total_times[t] = t-1 ~ t초까지 방영중인 방송의 수

    for i in range(1, play_time):
        total_times[i] += total_times[i - 1]

    # total_times[t] = 0 ~ t초까지 방영된 방송들의 시간의 합

    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            temp = total_times[i] - total_times[i - adv_time]
        else:
            temp = total_times[i]

        if temp > max_time:
            max_time = temp
            answer = i - adv_time + 1

    return convert2time(answer)


# test
print(solution(eval(input()), eval(input()), eval(input())))