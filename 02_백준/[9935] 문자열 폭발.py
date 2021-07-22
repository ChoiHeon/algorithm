# https://www.acmicpc.net/problem/9935


s, p = [*input()], [*input()]
ret = []
for i in range(len(s)):
    ret.append(s[i])
    if len(ret) >= len(p) and ret[-1] == p[-1]:
        for j in range(1, len(p)+1):
            if p[-j] != ret[-j]:
                break
        else:
            for _ in range(len(p)):
                ret.pop()
print(''.join(ret) if ret else "FRULA")