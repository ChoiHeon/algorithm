import sys

for case in range(int(sys.stdin.readline())):
    triangle = []
    for h in range(int(sys.stdin.readline())):
        triangle.append([int(i) for i in sys.stdin.readline().split()])

    for y in range(1, len(triangle)):
        triangle[y][0] += triangle[y-1][0]
        for x in range(1, len(triangle[y])-1):
            triangle[y][x] += max(triangle[y-1][x-1], triangle[y-1][x])
        triangle[y][len(triangle[y])-1] += triangle[y-1][len(triangle[y])-2]

    print(max(triangle[len(triangle)-1]))
    
        
        
