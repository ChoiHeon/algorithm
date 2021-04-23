# https://www.acmicpc.net/problem/1208


"""
주어진 a의 길이 N의 최대값이 40이므로 모든 경우의 수는 2^40 => 시간초과
하지만 a를 반으로 나누면 2^2 = 약 1000,000d => 시간내에 충분히 가능

a를 반으로 나눈 다음 모든 각각 경우의 수를 계산한 후,
합이 S가 되는 경우를 구합니다.
"""


from collections import Counter

n, s = map(int, input().split())
a = [*map(int, input().split())]
l_a = a[:n//2]
r_a = a[n//2:]
l_s = [0]
r_s = [0]

for x in l_a:
    l_s += [x+y for y in l_s]
for x in r_a:
    r_s += [x+y for y in r_s]

l_cntr = Counter(l_s)
r_cntr = Counter(r_s)
answer = -1 if s == 0 else 0

for l in l_cntr:
    if s-l in r_cntr:
        r = s-l
        answer += l_cntr[l]*r_cntr[r]

print(answer)



