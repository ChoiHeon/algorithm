# https://programmers.co.kr/learn/courses/30/lessons/17681


def solution(n, arr1, arr2):
    new_arr = [p|q for p, q, in zip(arr1, arr2)]
    new_arr = [bin(n)[2:] for n in new_arr]

    for i in range(n):
        if len(new_arr[i]) < n:
            new_arr[i] = '0'*(n-len(new_arr[i])) + new_arr[i]

    for i in range(n):
        new_arr[i] = new_arr[i].replace('1', '#')
        new_arr[i] = new_arr[i].replace('0', ' ')

    return new_arr


print(solution(eval(input()), eval(input()), eval(input())))
