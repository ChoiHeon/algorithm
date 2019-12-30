# https://www.acmicpc.net/problem/2579

'''

* 문제 분석
    - 첫 입력에서 주어지는 계단의 개수 만큼, 1과 2의 조합을 통해 최대값을 계산
    - 제약조건: 1을 연속으로 조합할 수 없음
    - 해결방한: 2개의 2차원 배열을 사용
                최대값을 저장하는 배열 & 이전의 선택(1 or 2)을 저장하는 배열

'''

N = int(input())

stairs = []
for _ in range(N):
    stairs.append(int(input()))

one_step = [0] * N      # value about moving one step
two_step = [0] * N      # value about moving two steps

one_step[0] = stairs[0]
one_step[1] = one_step[0] + stairs[1]
two_step[1] = stairs[1]

for i in range(2, N):
    if one_step[i - 1] != 0:
        one_step[i] = two_step[i - 1] + stairs[i]
    two_step[i] = max(one_step[i - 2], two_step[i - 2]) + stairs[i]

print(max(one_step[N - 1], two_step[N - 1]))

'''
max_value_list = [0] * N
pre_move_list  = [0] * N

max_value_list[0] = stairs[0]
max_value_list[1] = sum(stairs[0:2])
pre_move_list[1] = 1

for i in range(2, N):
    if pre_move_list[i - 1] == 1:
        max_value_list[i] = max_value_list[i - 2] + stairs[i]
    elif max_value_list[i - 1] > max_value_list[i - 2]:
        max_value_list[i] = max_value_list[i - 1] + stairs[i]
        pre_move_list[i] = 1
    else:
        max_value_list[i] = max_value_list[i - 2] + stairs[i]

print(max_value_list[N - 1])
print(max_value_list)
print(pre_move_list)
'''





