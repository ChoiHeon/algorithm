import sys


def check_level(sub_pi):
    n = len(sub_pi)
    interval = sub_pi[0] - sub_pi[1]

    if interval == 0:
        for i in range(1, n-1):
            if sub_pi[i] - sub_pi[i+1] != 0:
                return 10
        return 1
    elif abs(interval) == 1:
        flag = True
        for i in range(1, n-1):
            if flag and sub_pi[i] - sub_pi[i + 1] != interval:
                flag = False
        if flag:
            return 2

    flag = True
    for i in range(1, n-1):
        if flag and interval != ((sub_pi[i] - sub_pi[i+1]) * ((-1) ** i)):
            flag = False
    if flag:
        return 4

    flag = True
    for i in range(1, n - 1):
        if flag and interval != (sub_pi[i] - sub_pi[i + 1]):
            flag = False
    if flag:
        return 5

    return 10


cache = [-1] * 10002


def min_level(pi, begin):
    global cache
    if begin  == len(pi):
        return 0

    ret = cache[begin]
    if ret != -1:
        return ret

    ret = 999999999
    for i in range(3, 6):
        if begin + i <= len(pi):
            ret =  min(ret, min_level(begin + i, pi) + check_level(pi[begin:begin+i-1]))

    return ret


for case in range(int(sys.stdin.readline())):
    pi = int(sys.stdin.readline())
    print(min_level(pi, 0))


    
