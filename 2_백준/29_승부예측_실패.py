def find_index(array, e):
    cnt = array.count(e)
    ret = []
    for _ in range(cnt):
        ret.append(array.index(e))
        array[array.index(e)] = -1
    return ret

countries = input().split()
scores = [0] * 4
for _ in range(6):
    info = input().split()
    scores[countries.index(info[0])] += (float(info[2])*3 + float(info[3]))
    scores[countries.index(info[1])] += (float(info[4])*3 + float(info[3]))

temp = scores.copy()
answer = [0] * 4
for _ in range(2):
    score = max(temp)
    cnt = temp.count(score)
    for i in find_index(scores.copy(), score):
        answer[i] += 1 / cnt
    temp[temp.index(score)] = -1

for p in answer:
    print(p)