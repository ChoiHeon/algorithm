# https://www.acmicpc.net/problem/2839


"""
수학 카테고리에 있는 문제...지만
브루탈 포스처럼 모든 경우의 수를 체크하는 문제
다만 최소 계산 횟수를 찾는 문제이므로
3과 5의 값의 차이를 고려하여 정답을 탐색해야 함
"""


N = int(input())
b = 0
for _ in range(N//3, -1, -1):
    if N % 5 == 0:
        a = N // 5
        break
    N -= 3
    b += 1
print(-1) if N < 0 else print(a+b)
