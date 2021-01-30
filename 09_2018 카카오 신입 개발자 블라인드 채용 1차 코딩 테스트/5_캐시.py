# https://programmers.co.kr/learn/courses/30/lessons/17680


def solution(cacheSize, cities):
    from collections import Counter

    cache = set()
    last_visited = Counter()
    cities = [*map(lambda e: e.upper(), cities)]
    answer = 0

    for i in range(len(cities)):
        last_visited[cities[i]] = max(i, last_visited[cities[i]])
        if cities[i] in cache:
            answer += 1
        else:
            answer += 5
            if cacheSize == 0:
                continue

            if len(cache) == cacheSize:
                oldest = min([last_visited[city] for city in cache])
                for city in cache.copy():
                    if last_visited[city] == oldest:
                        cache.remove(city)
                        break
            cache.add(cities[i])

    return answer


print(solution(eval(input()), eval(input())))
