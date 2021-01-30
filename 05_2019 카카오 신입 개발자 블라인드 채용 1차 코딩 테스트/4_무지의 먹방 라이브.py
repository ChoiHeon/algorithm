# coding=utf-8
# https://programmers.co.kr/learn/courses/30/lessons/42891


"""
* 효율성 검사에서 많이 막힌 문제
* 풀이
    - 각 시간에 대해 인덱스르 저장 (enumerate 를 사용)
    - 시간에 대해 오름차순으로 정렬, 가장 앞의 시간이 최소 시간
    - (최소 시간 * 남은 음식의 수)가 k보다 클 때 까지 반복
    - 남은 음식들을 인덱스 순으로 정렬한 다음, k % (남은 음식의 수)가 가리키는 인덱스를 출력

* 효율성 요소
    - 남은 시간들에 대해 최소 시간을 뺄 필요 없음, 이전 시간만 기록하면 됨
    - 이전 시간을 빼는 것하고 매번 과거 시간의 차이를 누적한 것하고 같기 때문
"""


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    food_cnt = len(food_times)
    food_times = sorted(enumerate(food_times), key=lambda e: e[1])
    prev_time = 0

    for i in range(food_cnt):
        if food_times[i][1] == prev_time:
            continue
        if (food_cnt-i) * (food_times[i][1]-prev_time) > k:
            return sorted(food_times[i:])[k % (food_cnt - i)][0] + 1
        else:
            k -= (food_cnt-i) * (food_times[i][1]-prev_time)
        prev_time = food_times[i][1]


print(solution([3, 1, 2], 5))


