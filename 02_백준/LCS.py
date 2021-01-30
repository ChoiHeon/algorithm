# https://www.acmicpc.net/problem/9251


A, B = input(), input()
N, M = len(A), len(B)
dp = [[0] * (M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + (A[i-1] == B[j-1]))
print(dp[N][M])

'''
숏코딩
t=input();r=input();a=[0]*len(r)
for i in range(len(t)):
  for j in range(len(r)-1,-1,-1):
    if t[i]==r[j]:a[j]=max(a[:j])+1 if j else 1
print(max(a))
'''