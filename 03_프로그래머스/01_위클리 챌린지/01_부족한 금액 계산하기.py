# https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    times = count * (count + 1) / 2
    total = price * times
    answer = (total - money) if total > money else 0

    return answer