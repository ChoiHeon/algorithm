# https://www.acmicpc.net/problem/1700


"""
1. 각 기기의 인덱스를 저장합니다.
2. 매 기기 차례마다 아래의 과정을 수행합니다.
    a. 콘센트에 빈자리가 있다면 기기를 콘센트에 추가
    b. 콘센트에 빈자리가 있다면 콘센트에 꽂힌 기기들 중 가장 나중에 사용되거나
        사용될 일이 없는 기기를 뽑습니다.
"""


from collections import defaultdict

n, k = map(int, input().split())
apps = [*map(int, input().split())]
app_dict = defaultdict(list)

for i in range(k):
    app_dict[apps[i]].append(i)

sockets = set()
answer = 0

for i in range(k):
    in_app = apps[i]
    app_dict[in_app].pop(0)
    if in_app in sockets:
        continue

    if len(sockets) == n:
        out_app, next_idx = -1, -1
        for app in sockets:
            if not app_dict[app]:
                out_app = app
                next_idx = 101
            elif app_dict[app][0] > next_idx:
                out_app = app
                next_idx = app_dict[app][0]
        sockets.remove(out_app)
        answer += 1

    sockets.add(in_app)

print(answer)

