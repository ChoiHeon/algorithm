# https://www.acmicpc.net/problem/1072


x, y = map(int, input().split())
z = int(y * 100 / x)
s, e = 1, 1000000000

while s < e:
    m = (s + e) // 2
    m_z = int((y + m) * 100 / (x + m))

    if m_z <= z:
        s = m + 1
    else:
        e = m

print(e if int((y + e) * 100 / (x + e)) != z else -1)