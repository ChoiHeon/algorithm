import sys


def lis(p):
    if not p:   # check is empty
        return 0

    max_e = max(p)
    cache = [max_e + 1] * (len(p) + 1)

    for i in range(len(p)):  # check 0:i slice
        for j in range(i + 1):    # check j length
            if p[i] < cache[j] and p[i] not in cache[0:j]:
                cache[j] = p[i]
                break

    return cache.index(max_e + 1)


for case in range(int(sys.stdin.readline())):
    sys.stdin.readline()
    p = [int(c_int) for c_int in sys.stdin.readline().split()]
    print(lis(p))