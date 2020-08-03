# coding=utf-8
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231


for case in range(1, int(input()) + 1):
    n = int(input())
    a = n - 1

    def change(x):
        return int(str(x).replace('4', '3'))

    while True:
        a = change(a)
        b = n - a

        if '4' not in str(b):
            print("Case #{}: {} {}".format(case, a, b))
            break

        a, b = b, a

