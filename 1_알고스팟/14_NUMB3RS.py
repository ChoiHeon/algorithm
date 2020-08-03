import sys


for case in range(int(sys.stdin.readline())):
    # vertax count, days, prison position
    n, d, p = list(map(int, sys.stdin.readline().split()))

    # graph
    w = []
    for i in range(n):
        w.append(list(map(int, sys.stdin.readline().split())))

    # target_count, target_vertaxs
    target_count = int(sys.stdin.readline())
    target_vertax = list(map(int, sys.stdin.readline().split()))


    # Adjacent vertaxs and edge count about each vertax
    adj_vertax = [[] for v in range(n)]
    adj_edge = [0] * n
    for i in range(n):
        for j in range(n):
            if w[i][j] == 1:
                adj_vertax[i].append(j)
                adj_edge[i] += 1
                
    '''
    available[k][i] = sum(available[k-1][j] / adj_edge[j])
    --> vertax_j is adjacent vertaxs of vertax_i
    '''
    available = [[0]*n for i in range(d+1)]
    available[0][p] = 1
    for k in range(1, d+1):
        for i in range(n):
            for j in adj_vertax[i]:
                available[k][i] += available[k-1][j] / adj_edge[j]

    # print solution
    for v in target_vertax:     
        print('{0:.8f}'.format(available[d][v]), end=' ')
    print('\n')
