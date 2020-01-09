# https://www.acmicpc.net/problem/1012

# 파이썬의 기본 재귀횟수는 1000
# 별도의 코드를 통해 제한을 늘려야 함
import sys
sys.setrecursionlimit(10**6)


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    w = [[0] * n for _ in range(m)]
    for __ in range(k):
        x, y = map(int, input().split())
        w[x][y] = 1
    answer = 0
    for i in range(m):
        for j in range(n):
            def check(p, q):
                global w
                if 0 <= p < m and 0 <= q < n and w[p][q]:
                    w[p][q] = 0
                    check(p-1, q); check(p+1, q); check(p, q-1); check(p, q+1)
                return
            if w[i][j]:
                check(i, j)
                answer += 1
    print(answer)


# 숏코딩
# range 대신 [0]*을 통해 반복문을 구현
# 출력값이 단순히 정수 하나이므로 아래와 같은 방법으로 출력값을 저장시킬 변수를 지정하지 않아도 됨
for r in[0]*int(input()):

    # '*'을 통해 iterator타입의 객체를 unpacking
    # 끝에 ,를 추가하여 단순 괄호()가 아닌 tuple임을 암시
     d={(*map(int,input().split()),)for _ in[0]*int(input().split()[2])}

    # d가 empty일 때 까지 반복
     while d:

         # dictionary의 pop은 앞에서 시작함 (list는 뒤, tuple은 pop을 제공하지 않음)
          s=[d.pop()];r+=1

         # DFS 시작 (list는 뒤에서부터 pop하기 때문)
          while s:
               x,y=s.pop()


               for e in-2,0,2,4:
                   # 두 값을 ,로 나누어 표현할 경우 tuple타입의 객체로 저장
                   # 파이썬에서 음수에 //를 사용할 경우, -5 // 3 --> 3 * (-2) + ? 이기 때문에 -2를 반환한다
                   # 음수의 나머지 연산의 경우 -7=3*-3 + 2 이기 때문에 -7%3 = 2이다 (음수 나머지를 허용하지 않음)
                   # 위의 연산은 언어에 따라 차이가 있으며, C의 경우 음수 나머지를 허용하기 때문에 답은 -1이다
                   # 결과적으로 아래 연산은 순서대로 좌, 상, 우, 하의 좌표를 의미한다
                    p=x+e//3,y+e%3-1

                    # dictionary의 비교 연산자는 포함 관계를 의미
                    # {1, 2, 3} > {1, 2}    --> True
                    # {1, 2} >= {1, 2}      --> False
                    # {1, 7} >= {1, 2}      --> False
                    # -=연산을 통해 중복된 요소만 제거한다
                    # {1, 2, 3} - {1} = {2, 3}
                    # {1, 2, 3} - {1, 7} = {2, 3}
                    # 이와 같은 연산은 list와 tuple은 제공하지 않음
                    # s+=p,에서 마지막에 ,를 더함으로 인해 tuple자체가 원소로 list에 append
                    # 즉, ','를 통해 tuple을 packing
                    if{p}<=d:d-={p};s+=p,
     print(r)


