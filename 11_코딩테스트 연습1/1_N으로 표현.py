# https://programmers.co.kr/learn/courses/30/lessons/42895


def solution(N, number):
    if N == number: return 1
    dp = [{}, {N}]
    for i in range(2, 9):
        tmp = {int(str(N)*i)}
        for j in range(1, i//2+1):
            for p in dp[j]:
                for q in dp[i-j]:
                    tmp.update([p+q, p*q])
                    if abs(p-q) != 0:           tmp.add(abs(p-q))
                    if p%q == 0 and p//q != 0:  tmp.add(p//q)
                    if q%p == 0 and q//p != 0:  tmp.add(q//p)
        if number in tmp:   return i
        dp.append(tmp)
    return -1


print(solution( eval(input()), eval(input())))