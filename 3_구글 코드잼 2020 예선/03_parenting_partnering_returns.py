# 구글 코드잼 2020 예선

for case in range(1, int(input())+1):
    n = int(input())
    m = sorted([[*(map(int, input().split())), i] for i in range(n)], key=lambda e: e[0:1])
    s = [(-1, -1), (-1, -1)]
    is_busy = [False, False]
    answer = [-1] * n

    for e in m:
        for i in range(2):
            if s[i][1] <= e[0]:
                is_busy[i] = False

        if not is_busy[0]:
            s[0] = e
            is_busy[0] = True
            answer[e[2]] = 'C'
        elif not is_busy[1]:
            s[1] = e
            is_busy[1] = True
            answer[e[2]] = 'J'
        else:
            answer = ["IMPOSSIBLE"]
            break

    print("Case #{}: ".format(case) + ''.join(answer))
