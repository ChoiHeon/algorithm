# https://www.acmicpc.net/problem/7579


"""
dp[i][j] = 0 ~ i 까지 아이템과 최대 j 비용을 이용하여 얻을 수 있는 최대 메모리
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
m = [*map(int, input().split())]
c = [*map(int, input().split())]
d = [0] * 10000
s = sum(c)

for i in range(N):
    for j in range(s, c[i]-1, -1):      # 거꾸로 할 경우, 자연스럽게 d[j]은 i-1를 활용한 값이 사용된다
        d[j] = max(d[j], d[j-c[i]] + m[i])
    print(d)


answer = 0
while answer < s and d[answer] < M:
    answer += 1

print(answer)