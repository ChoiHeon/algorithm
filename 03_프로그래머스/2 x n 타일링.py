# https://programmers.co.kr/learn/courses/30/lessons/12900

"""
dp로 접근 가능한 문제
dp[n] = 2xn 직사각형을 해울 수 있는 방법의 수
dp[i] = dp[i-1] + dp[i-2] (i > 2)
--> 피보나치 수열과 동일
"""

def solution(n):
    a = b = 1
    for _ in range(n):
        a, b = b, a+b
    return a % 1000000007


print(solution(eval(input())))