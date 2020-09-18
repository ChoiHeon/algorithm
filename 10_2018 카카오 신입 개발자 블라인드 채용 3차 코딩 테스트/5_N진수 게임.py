# https://programmers.co.kr/learn/courses/30/lessons/17687


def n_ary(n, v):
    ret = []
    while v:
        ret.append(v%n)
        v = v // n
    ret.reverse()
    return ret if ret else [0]


def solution(n, t, m, p):
    numbers = []
    for i in range(t*m):
        numbers += n_ary(n, i)

    convert = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    for i in range(10):
        convert[i] = i

    return ''.join(map(str, [convert[numbers[(p-1)+(i*m)]] for i in range(t)]))



print(solution(eval(input()), eval(input()), eval(input()), eval(input())))
