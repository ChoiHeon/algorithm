# https://www.acmicpc.net/problem/1712

A, B, C = map(int, input().split())
print(A // (C - B) + 1) if B < C else print(-1)


'''
숏코딩
print(-(B>=C) or (A//(C-B)+1))
'''

'''
print(논리연산자)
or은 앞의 operand가 True일 경우 뒤의 operand를 확인하지 않음
and는 무조건 뒤의 식을 출력
'''