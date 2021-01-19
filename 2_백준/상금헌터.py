# https://www.acmicpc.net/problem/15953

s = [sum(range(x+1)) for x in range(1, 7)] + [100]
t = [2**x-1 for x in range(1, 6)] + [64]
p = list(map(lambda x: x*10000, [500, 300, 200, 50, 30, 10, 0]))
q = list(map(lambda x: x*10000, [512, 256, 128, 64, 32, 0]))

for _ in range(int(input())):
    def f(a, b):
        if a:
            for i in range(7):
                if a <= s[i]:
                    a = p[i]
        if b:
            for i in range(6):
                if b <= t[i]:
                    b = q[i]
        return a+b
    print(f(*map(int, input().split())))

# 숏코딩
# 위의 함수를 통해 상금을 찾는 과정을 아래와 같이 줄임
a=[0,500]+[300]*2+[200]*3+[50]*4+[30]*5+[10]*6+[0]*90
b=[0,512]+[256]*2+[128]*4+[64]*8+[32]*16+[0]*90
exec("x,y=map(int,input().split());print((a[x]+b[y])*10000);"*int(input()))
