# https://programmers.co.kr/learn/courses/30/lessons/17686


def solution(files):
    import re

    m = re.compile("([^\d]+)(\d{1,5})(.*)")
    for i in range(len(files)):
        files[i] = re.match(m, files[i]).groups()

    files.sort(key=lambda e: (e[0].casefold(), int(e[1])))
    files = [*map(lambda e: ''.join(e), files)]

    return files


print(solution(eval(input())))
