# https://www.acmicpc.net/workbook/view/1152
# https://www.acmicpc.net/problem/2252


"""
* 위상정렬 문제
    - 리스트의 원소들 중 일부의 순서가 주어짐
    - 주어진 순서에 위배되지 않도록 리스트를 정렬
    - 일종의 그래프 문제로 들어오는 간선이 없는 노드를 시작으로 큐를 이용한 DFS 사용
    - 큐에서 pop한 원소A가 가리키는 원소B에 대해 만약 B에 들어오는 간선이 없는 경우 큐에 push
    - 큐가 빌 때까지 반복
    - 아래 문제의 경우 복수의 답이 가능
"""


from collections import deque


n, m = map(int, input().split())
next = {i: set() for i in range(1, n+1)}
prev = {i: set() for i in range(1, n+1)}
for _ in range(m):
    a,b = map(int, input().split())
    next[a].add(b)
    prev[b].add(a)

answer = []
queue = deque(filter(lambda e: not prev[e], range(1, n+1)))

while queue:
    stud = queue.popleft()
    answer.append(stud)
    for i in next[stud]:
        prev[i].remove(stud)
        if not prev[i]:
            queue.append(i)
    del next[stud]

print(' '.join(map(str, answer)))












