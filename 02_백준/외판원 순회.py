# https://www.acmicpc.net/problem/11723


"""
* 비트마스크를 이용한 부분집합 구현
    - i 활성화:        b | (1 << i)
    - i 비활성화:      b & ~1 << i)
    - i 활성화 여부:   b & (1 << i)

* dp[cur][visited]
    - cur = 현재 정점
    - visited = 방문한 정점을 비트마스크로 표현 --> 방문하지 않은 정점들을 의미할 수도 있음
    - dp[cur][visited] = 현재 정점(cur)에서 방문하지 정점들(visited)을 이용해 순환했을 경우 얻을 수 있는 최소 비용
"""

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
bm = 2**n-1     # (1 << n) - 1
w = [list(map(lambda e: int(e) if int(e) else float('inf'), input().split())) for _ in range(n)]
dp = [[0] * bm for _ in range(n)]


def tsp(x, bm):
    if not bm:
        return w[x][0]

    if dp[x][bm]:
        return dp[x][bm]

    ret = float('inf')
    for i in range(n):
        if bm & (1 << i) and w[x][i] != float('inf'):
            ret = min(ret, w[x][i] + tsp(i, bm & ~(1 << i)))

    dp[x][bm] = ret
    return ret


print(tsp(0, bm-1))
