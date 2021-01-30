# coding=utf-8
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da


for case in range(1, int(input()) + 1):
    n = int(input())
    rival = input()
    me = ''.join(map(lambda e: 'S' if e == 'E' else 'E', rival))
    
    print("Case #%d: %s" % (case, me))
    
            


