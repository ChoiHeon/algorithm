# https://www.acmicpc.net/problem/15956


"""

"""


S = input().split("&&")
dic = {}
cnt = 0
same = []
diff = []
words = []
parents = []


def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    a = find(dic[x])
    b = find(dic[y])
    if a != b:
        if len(x) < len(y):
            parents[b] = a
        else:
            parents[a] = b


for sub in S:
    if '!' in sub:
        p, q = sub.split("!=")
        diff.append(sub)
        flag = False

    else:
        p, q = sub.split("==")
        same.append(sub)
        flag = True

    for r in [p, q]:
        if r not in dic.keys():
            dic[r] = cnt
            parents.append(cnt)
            cnt += 1
            if flag:
                words.append(r)

# 등호로 연결된 단어끼리 union
for s in same:
    i, j = s.split("==")
    union(i, j)

answer = []

for w in words:
    if dic[w] != find(dic[w]):
        answer.append("{}=={}".format(w, list(dic.keys())[find(dic[w])]))

for d in diff:
    p, q = d.split("!=")
    answer.append("{}!={}".format(list(dic.keys())[find(dic[p])], list(dic.keys())[find(dic[q])]))

for ans in answer[:len(answer)-1]:
    print(ans, end="&&")
print(answer[-1])

# 수식 중복 처리할 것

