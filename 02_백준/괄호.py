# https://www.acmicpc.net/problem/9012


for _ in range(int(input())):
    ps = input()
    stack = 0

    for p in ps:
        if p == '(':
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                break

    print("NO" if stack else "YES")