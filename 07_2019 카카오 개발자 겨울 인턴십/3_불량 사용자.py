# https://programmers.co.kr/learn/courses/30/lessons/64064


def solution(user_id, banned_id):
    import re
    from itertools import permutations

    banned_id = list(map(lambda e: e.replace('*', '.') + '$', banned_id))
    candidates = []

    for ids in permutations(list(user_id), len(banned_id)):
        same = True
        for id, ban in zip(ids, banned_id):
            if not re.match(ban, id):
                same = False
                break
        if same:
            candidates.append(ids)

    candidates = list(map(lambda e: tuple(sorted(e)), candidates))
    return len(set(candidates))


print(solution(eval(input()), eval(input())))
