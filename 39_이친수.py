# https://www.acmicpc.net/problem/2193


dp = [[1, 1] for _ in range(int(input())-1)]
for i in range(1, len(dp)):
    dp[i][0] = sum(dp[i-1])
    dp[i][1] = dp[i-1][0]
print(dp[-1][0]) if len(dp) else print(1)

# 결론적으로 피보나치수열을 구하는 문제
'''
숏코딩
a,b=0,1
exec('a,b=b,a+b;'*int(input()))
print(a)
'''