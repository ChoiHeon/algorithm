# https://programmers.co.kr/learn/courses/30/lessons/17683

def solution(m, musicinfos):
    import re

    convert = {"C#":"Q", "D#":"W", "F#":"R", "G#":"T", "A#":"Y"}
    m = re.findall("[A-Z][^A-Z]?", m)
    m = [*map(lambda e: e if e not in convert.keys() else convert[e], m)]
    m = ''.join(m)
    musicinfos = [*map(lambda e: e.split(','), musicinfos)]
    answer = [0, "(None)"]

    for info in musicinfos:
        info[0] = [*map(int, info[0].split(':'))]
        info[1] = [*map(int, info[1].split(':'))]
        play_time = (info[1][0]-info[0][0])*60 + info[1][1]-info[0][1]

        info[3] = re.findall("[A-Z][^A-Z]?", info[3])
        info[3] = [*map(lambda e: e if e not in convert.keys() else convert[e], info[3])]
        music_len = len(info[3])

        info[3] = info[3]*(play_time//music_len) + info[3][0:play_time%music_len]
        if m in ''.join(info[3]) and answer[0] < play_time:
            answer = [play_time, info[2]]

    return answer[1]


print(solution(eval(input()), eval(input())))
