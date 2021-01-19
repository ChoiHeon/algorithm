# https://www.acmicpc.net/problem/1152
s = input()
print(s.strip().count(' ') + 1) if s.count(' ') != len(s) else print(0)


'''
# 숏코딩
print(len(input().split()))
'''
