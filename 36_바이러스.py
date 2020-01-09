# https://www.acmicpc.net/problem/2606

import queue

N = int(input())
w = [[0]*(N+1) for _ in range(N+1)]
for _ in range(int(input())):
    p, q = map(int, input().split())
    w[p][q] = w[q][p] = 1
answer = 0
q = queue.Queue()
q.put(1)
for k in range(N + 1):
    w[k][1] = 0
while not q.empty():
    t = q.get()
    for i in range(1, N+1):
        if w[t][i] == 1:
            for j in range(N+1):
                w[j][i] = 0
            q.put(i)
            answer += 1
print(answer)

'''
def r(s):
 if c[s]==1:return
 c[s]=1
 for i in l[s]:r(i)
input()
s=int(input())
l=[[]*s for i in range(101)]
c=[0]*101
for i in range(s):
 a,b=map(int,input().split())
 l[a].append(b)
 l[b].append(a)
r(1)
s=0
for i in c:s+=i
print(s-1)
'''