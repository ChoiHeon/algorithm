# coding=utf-8
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231


for case in range(1, int(input()) + 1):
    n = input()
    a = ''

    for i in range(len(n)):
        a += '1' if n[i] == '4' else '0'

    a = int(a)
    b = int(n) - a
    print("Case #{}: {} {}".format(case, a, b))

