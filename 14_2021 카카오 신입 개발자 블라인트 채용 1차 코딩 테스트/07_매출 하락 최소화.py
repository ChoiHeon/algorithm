# https://programmers.co.kr/learn/courses/30/lessons/72416

"""
dp[i][0] = i를 루트로 하는 서브트리에서 i를 택하지 않았을 때, 최소 매출 하락액
dp[i][1] = i를 루트로 하는 서브트리에서 i를 택했을 때, 최소 매출 하락액
"""


from collections import defaultdict, deque


def solution(sales, links):
    n = len(sales)
    dp = [[0, 0] for _ in range(n)]
    tree = defaultdict(list)
    level = defaultdict(list)

    for a, b in links:
        tree[a - 1].append(b - 1)

    queue = deque()
    queue.append((0, 0))

    while queue:
        i, l = queue.popleft()
        level[l].append(i)
        for j in tree[i]:
            queue.append((j, l + 1))

    for l in sorted(level.keys(), key=lambda e:-e):
        for i in level[l]:
            # i를 택한 경우
            dp[i][1] = sales[i]
            for j in tree[i]:
                dp[i][1] += min(dp[j])

            # i를 택하지 않은 경우
            temp = []
            for j in tree[i]:
                temp.append(dp[j][1])
                for k in tree[i]:
                    if k != j:
                        temp[-1] += min(dp[k])
            dp[i][0] = min(temp) if temp else 0

    return min(dp[0])


print(solution(eval(input()), eval(input())))