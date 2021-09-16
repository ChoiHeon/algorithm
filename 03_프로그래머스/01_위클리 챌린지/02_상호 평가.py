# https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(scores):
    from collections import Counter

    rank = {50: 'F', 70: 'D', 80: 'C', 90: 'B', 101: 'A'}
    score_avg = [0] * len(scores)
    answer = [''] * len(scores)

    for i in range(len(scores)):
        self_score = scores[i][i]
        min_score = 101
        max_score = -1
        score_counter = Counter()

        for j in range(len(scores)):
            score_counter[scores[j][i]] += 1
            max_score = max(scores[j][i], max_score)
            min_score = min(scores[j][i], min_score)

        if (self_score == max_score or self_score == min_score) and score_counter[self_score] == 1:
            del score_counter[self_score]

        score_avg[i] = sum([k * v for k, v in score_counter.items()]) / sum(score_counter.values())

    for i in range(len(score_avg)):
        for k, v in rank.items():
            if score_avg[i] < k:
                answer[i] = v
                break

    return ''.join(answer)