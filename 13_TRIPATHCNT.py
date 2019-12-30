import sys


'''
# time over code
def path(y, x):
    global triangle
    if y == 1 or x == 0 or x == (len(triangle[y]) - 1):
        return 1
    if triangle[y-1][x-1] > triangle[y-1][x]:
        return path(y-1, x-1)
    elif triangle[y-1][x-1] < triangle[y-1][x]:
        return path(y-1, x)
    else:
        return path(y-1, x) + path(y-1, x-1)
'''


for case in range(int(sys.stdin.readline())):
    triangle = []
    n = int(sys.stdin.readline())
    path = [[1] * n for raw in range(n)]

    for h in range(n):
        triangle.append([int(i) for i in sys.stdin.readline().split()])

    for y in range(1, len(triangle)):
        triangle[y][0] += triangle[y-1][0]
        for x in range(1, len(triangle[y])-1):
            if triangle[y - 1][x - 1] > triangle[y - 1][x]:
                path[y][x] = path[y-1][x-1]
                triangle[y][x] += triangle[y - 1][x - 1]
            elif triangle[y - 1][x - 1] < triangle[y - 1][x]:
                path[y][x] = path[y-1][x]
                triangle[y][x] += triangle[y - 1][x]
            else:
                path[y][x] = path[y-1][x-1] + path[y-1][x]
                triangle[y][x] += triangle[y - 1][x - 1]
        triangle[y][len(triangle[y])-1] += triangle[y-1][len(triangle[y])-2]

    max_value = max(triangle[n-1])
    print(sum([path[n-1][x] for x in range(n) if triangle[n-1][x] == max_value]))
