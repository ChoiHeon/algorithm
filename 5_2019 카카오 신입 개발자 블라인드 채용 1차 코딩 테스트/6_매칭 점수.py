# coding=utf-8
# https://programmers.co.kr/learn/courses/30/lessons/42893

# 정규 표현식 참고: http://www.nextree.co.kr/p4327/


import re


def solution(word, pages):
    n = len(pages)
    url_index = dict()
    basic_scores = [0] * n
    link_counts = [0] * n
    link_scores = [0] * n
    external_links = [[] for _ in range(n)]

    for i in range(n):
        url = re.findall("<meta property=\"og:url\" content=\"(.+?)\"/>", pages[i])[0]
        url_index[url] = i
        basic_scores[i] = re.sub("[^a-z]+", '.', pages[i].lower()).split('.').count(word.lower())
        for link in re.findall("<a href=\"(.+?)\">", pages[i]):
            link_counts[i] += 1
            external_links[i].append(link)

    for i in range(n):
        score = (basic_scores[i] / link_counts[i]) if link_counts[i] else 0
        for link in external_links[i]:
            if link in url_index.keys():
                link_scores[url_index[link]] += score

    matching_score = list(map(sum, zip(basic_scores, link_scores)))
    return matching_score.index(max(matching_score))


input_data = input()
print(solution("blind", eval(input_data)))