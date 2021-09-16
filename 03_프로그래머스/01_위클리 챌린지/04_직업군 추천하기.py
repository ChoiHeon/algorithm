# 프로그래머스 위틀리 챌린지 4주차
# 문제: 직업군 추천하기
# link: https://programmers.co.kr/learn/courses/30/lessons/84325


def solution(table, languages, preference):
    max_score = -1
    answer = []
    table = list(map(lambda e: e.split(), table))
    job_lang = {table[i][0]: table[i][1:] for i in range(5)}
    lang_pref = {languages[i]: preference[i] for i in range(len(languages))}

    for j, l in job_lang.items():
        score = sum(map(lambda i: (5 - i) * (lang_pref[l[i]] if l[i] in lang_pref.keys() else 0), range(5)))
        if score > max_score:
            max_score = score
            answer = [j]
        elif (score == max_score):
            answer.append(j)

    return sorted(answer)[0]