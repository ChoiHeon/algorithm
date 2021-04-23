# https://www.acmicpc.net/problem/1629


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def func(a, b, c):
    if b == 1:
        return a%c
    if b%2== 0:
        return (func(a, b//2, c)**2)%c
    else:
        return (func(a, b//2, c)**2*a)%c


print(func(*map(int, input().split())))