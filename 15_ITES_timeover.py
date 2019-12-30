#Maybe It's impassible to success in time by Python

import sys
import queue


T = 2**32


for case in range(int(sys.stdin.readline())):
    k, n = list(map(int, sys.stdin.readline().split()))
    a = 1983
    q = queue.Queue()
    ret = 0
    for _ in range(n):
        i = (a % 10000) + 1
        q.put(k)
        for __ in range(q.qsize() - 1):
            j = q.get()
            if j > i:
                q.put(j - i)
                continue
            elif j == i:
                ret += 1
        a = (a * 214013 + 2531011) % T
    print(ret)

    
                
                
        
