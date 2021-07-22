# 문제: https://www.acmicpc.net/problem/14888
# 코드길이: 564 Byte
# 시간: 2284 ms

"""
모든 수열, 조합을 고려해야 하는 경우 permutations 혹은 combinations 를 사용하는 것이 용이
permutations 를 사용할 때 인자로 들어가는 iterable 내에 중복되는 원소가 있는 경우,
set을 통해 중복되는 경우를 제거해야 한다
"""

from itertools import permutations

# 입력 받은 데이터 저장
input()
numbers = input().split()
op_count = list(map(int, input().split()))
op_symbol = ["/", "*", "-", "+"]
operators = []
for i in op_count:
    op = op_symbol.pop()
    for j in range(i):
        operators.append(op)

# 연산자에 대한 모든 경우의 조합 생성
op_combs = set(permutations(operators))
num_count = len(numbers)
result = []

# 모든 경우에 대한 연산
while op_combs:
    op_comb = op_combs.pop()
    num = int(numbers[0])
    for i in range(1, num_count):
        num = int(eval(str(num) + op_comb[i-1] + numbers[i]))
    result.append(num)

# 결과 출력
print(max(result))
print(min(result))

