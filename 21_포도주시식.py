# https://www.acmicpc.net/problem/2156

N = int(input())
p = []
dp = [0] * N

for _ in range(N):
    p.append(int(input()))

if N < 3:
    print(sum(p[0:N]))
elif N == 3:
    print(max(p[0] + p[1], max(p[0], p[1]) + p[2]))
else:
    # initialize
    dp[0] = p[0]
    dp[1] = dp[0] + p[1]
    dp[2] = max(dp[1], max(p[0], p[1]) + p[2])

    # loop
    for i in range(3, N):
        dp[i] = max(dp[i-3] + p[i-1] + p[i], dp[i-2] + p[i])
        dp[i] = max(dp[i-1], dp[i])

    print(dp[N-1])

'''
<Best PS>
import sys
I=sys.stdin.readline
a=[int(I())for i in range(int(I()))]
d=[0,a[0],0]
for i in a[1:]:
    d=[max(d),d[0]+i,d[1]+i]  
print(max(d))
'''