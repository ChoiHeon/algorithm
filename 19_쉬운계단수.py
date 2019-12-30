# https://www.acmicpc.net/problem/10844

N = int(input())

# 가장 큰 자릿수에 올 수 있는 숫자(index)의 개수
# ex) N = 1일 때, 자릿수에 올 수 있는 숫자 -> 0(숫자): 0(개), 1: 1, 2: 1, 3: 1, ..., 9: 1
numCounter = [[0] * 10 for _ in range(N)]

# 계단수를 생성하기 위해 파생되는 숫자
nextNumer = [[1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8]]

# N = 1일 경우를 초기화
numCounter[0] = [1] * 10

for i in range(1,N):
    for j in range(10):
        for k in nextNumer[j]:
            numCounter[i][k] += numCounter[i-1][j]

print(sum(numCounter[N-1][1:10]) % 1000000000)