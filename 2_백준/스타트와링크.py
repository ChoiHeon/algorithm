# 문제: https://www.acmicpc.net/problem/14889
# 코드길이: 557 Byte
# 시간: 3680 ms

"""
combinations 함수를 실행한 결과의 앞에서 i번째와 뒤에서 i번째의 조합의 원소가 겹치지 않음을 확인
이를 활용하여 주어진 0 ~ N-1 까지의 수를 2개의 그룹으로 분할
"""


from itertools import combinations


n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
combs = list(combinations(list(range(n)), int(n/2)))
ans = float("inf")

for i in range(len(combs)//2):
    team_a, team_b = combs[i], combs[-i-1]
    s_a, s_b = 0, 0
    for pair_a in list(combinations(team_a, 2)):
        s_a += (w[pair_a[0]][pair_a[1]] + w[pair_a[1]][pair_a[0]])
    for pair_b in list(combinations(team_b, 2)):
        s_b += (w[pair_b[0]][pair_b[1]] + w[pair_b[1]][pair_b[0]])
    ans = min(ans, abs(s_a-s_b))

print(ans)