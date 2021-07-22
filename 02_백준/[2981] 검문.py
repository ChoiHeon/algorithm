# https://www.acmicpc.net/problem/2981


def dividers(num):
    array = [num]

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if i * i == num:
                array.append(i)
            else:
                array.append(i)
                array.append(int(num / i))

    return sorted(array)


p = []
for _ in range(int(input())):
    p.append(int(input()))

p.sort()
q = dividers(p[-1] - p[0])

for i in q:
    k = p[0] % i
    flag = True

    for j in p[1:]:
        if j % i != k:
            flag = False
            break
    if flag:
        print(i, end=' ')
