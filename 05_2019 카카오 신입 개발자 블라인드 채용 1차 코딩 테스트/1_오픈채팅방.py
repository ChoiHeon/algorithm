# https://programmers.co.kr/learn/courses/30/lessons/42888


def solution(record):
    answer = []
    db = dict()
    record = list(map(lambda e: e.split(), record))

    for e in record:
        if e[0][0] == 'E' or e[0][0] == 'C':
            db[e[1]] = e[2]

    for e in record:
        if e[0][0] == 'E':
            answer.append("{}님이 들어왔습니다.".format(db[e[1]]))
        elif e[0][0] == 'L':
            answer.append("{}님이 나갔습니다.".format(db[e[1]]))
    return answer


input_data = input()
print(solution(eval(input_data)))

