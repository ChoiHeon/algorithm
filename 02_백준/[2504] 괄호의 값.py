# https://www.acmicpc.net/problem/2504


exp = input()
s = []
opp = {']':'[', ')':'('}
cov = {']':3, ')':2}

for e in exp:
    if e == '(' or e == '[':
        s.append(e)
    else:
        if not s:
            break
        if s[-1] == opp[e]:
            s[-1] = cov[e]
        elif type(s[-1]) == int:
            if len(s) < 2:
                s = [0]
                break
            if s[-2] == opp[e]:
                s[-2] = s[-1] * cov[e]
                s.pop()
            else:
                s = [0]
                break
    if len(s) >= 2:
        if type(s[-1]) == type(s[-2]) == int:
            s[-2] = s[-1] + s[-2]
            s.pop()

if len(s) == 1 and type(s[0]) == int:
    print(s[0])
else:
    print(0)
