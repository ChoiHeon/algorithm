# https://www.acmicpc.net/problem/9372

# 모든 노드들이 간선들로 연결되어 있음
# 그러므로 N-1개의 간선으로 모든 노드들을 방문 가능

i = sys.stdin.readline
for _ in range(int(i())):
    n, m = list(map(int, i().split()))
    for __ in range(m):
        i()
    print(n-1)

# BST 알고리즘 적용
'''
import queue

def success(p, n):
    ret = True
    for i in range(n):
        ret = ret and (i in p)
    return ret

for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    w = [[0]*n for _ in range(n)]

    for i in range(m):
        x, y = list(map(int, input().split()))
        w[x-1][y-1] = w[y-1][x-1] = 1

    q = queue.Queue()
    for i in range(n):
        q.put([i])

    while not q.empty():
        p = q.get()
        c = p[len(p)-1]
        for i in range(n):
            t = p.copy()
            if w[c][i] == 1:
                t.append(i)
                if success(t, n):
                    print(len(t)-1)
                    q.queue.clear()
                    break
                else:
                    q.put(t)
'''



