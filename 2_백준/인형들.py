# 문제: https://www.acmicpc.net/problem/15954
# 코드길이:  Byte
# 시간:  ms

"""
문제의 정확한 이해와 시간초과 주의
python3 형식으로 제출시 시간초과 발생
Pypy3 형식으로 제출함으로써 해결

아래의 코드에 적용하지 않았지만, Python의 float으로 테스트케이스 정답과의 오차가 발생할 수 있음
위의 오차로 인해 실패가 발생할 경우, decimal.Decimal를 사용하는 것을 추천
정확한 실수 표현과 다양한 입력 방식을 지원
"""


n, k = map(int, input().split())
pref = list(map(int, input().split()))
ans = float("inf")
for i in range(n-k+1):
    for j in range(k, n-i+1):
        sub_avg = sum(pref[i:i+j]) / j
        ans = min(ans, (sum(map(lambda e: (e-sub_avg)**2, pref[i:i+j])) / j)**0.5)
print(ans)






