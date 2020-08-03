# https://www.acmicpc.net/problem/1011

for i in range(int(input())):
    a, b = map(int, input().split())
    num = b-a
    i = j = 1
    while num > 0:
        num -= i
        i += 1
        if num >= j:
            num -= j
            j += 1
    print(i + j - 2)

'''
숏코딩
exec('a,b=map(int,input().split());print(int((4*(b-a)-3)**.5));'*int(input()))

아래와 같음
for _ in range(int(input())):
    a,b=map(int,input().split())
    print(int((4*(b-a)-3)**.5))
'''
