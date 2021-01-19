# https://programmers.co.kr/learn/courses/30/lessons/62048


"""
w와 h의 최소공배수가 1이 아닐 경우, 일정한 최소공배수 만큼의 반복이 발생
w와 h의 최소공배수가 1일 경우, 대각선에 의해 잘리는 사각형의 수는 w+h-1

즉, 전체 넓이(w*h)에서 부분적으로 잘리는 사각형의 수(w/gcd + h/gcd - 1)에 최소공배수(gcd)를 곱한 결과를 빼면 답을 구할 수 있다
= (w*h) - ((w+h-1) * gcd(w, h))
"""


def solution(w, h):
    def gcd(x, y):
        if y == 0:
            return x
        return gcd(y, x % y)

    return w * h - w - h + gcd(w, h)

print(solution(eval(input()), eval(input())))
