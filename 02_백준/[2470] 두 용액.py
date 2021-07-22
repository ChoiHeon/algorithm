# https://www.acmicpc.net/problem/2470


n = int(input())
liquids = sorted(map(int, input().split()))
low, high = 0, n-1
min_density = float('inf')
answer = [-1, -1]

while low < high:
    density = liquids[low]+liquids[high]

    if abs(density) < min_density:
        min_density = abs(density)
        answer[0], answer[1] = liquids[low], liquids[high]

    if density < 0:
        low += 1
    else:
        high -= 1

print(*answer)