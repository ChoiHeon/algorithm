from itertools import combinations

# main
# https://www.acmicpc.net/problem/2798

N, M = map(int, input().split())
arr = list(filter(lambda x: x < M, map(int , input().split())))
arr = sorted(list(map(sum, combinations(arr, 3))))
result = 0

for s in arr:
    result = s if result < s and s <= M else result

print(result)


'''
# for문으로 구현
best_sum = 0
arr_len = len(arr)

for i in range(arr_len - 2):
    for j in range(i + 1, arr_len - 1):
        for k in range(j + 1, arr_len):
            temp_sum = arr[i] + arr[j] + arr[k]
            best_sum = temp_sum if best_sum < temp_sum and temp_sum <= M else best_sum

print(best_sum)
'''


