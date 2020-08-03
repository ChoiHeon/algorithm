import sys


n = 0
array = []
cache = []


def init_cache():
    global cache
    cache = [[-1] * (n+1) for i in range(n)]
    for i in range(n):                  # begin
        for j in range(i + 1, n + 1):       # end
            avg = int(round(sum(array[i:j]) / (j - i)))
            cache[i][j] = sum(list(map(lambda x: (x - avg) ** 2, array[i:j])))


def quantize(begin, part):
    global array
    global n

    if part == 1:
        return cache[begin][n]

    ret = 987654321
    for end in range(begin + 1, n - part + 1):
        ret = min(ret, cache[begin][end] + quantize(end, part-1))

    return ret


for case in range(int(sys.stdin.readline())):
    temp = list(map(int, sys.stdin.readline().split()))
    n = temp[0]
    m = temp[1]
    array = sorted(list(map(int, sys.stdin.readline().split())))
    if n <= m:
        print(0)
    else:
        init_cache()
        print(quantize(0, m))