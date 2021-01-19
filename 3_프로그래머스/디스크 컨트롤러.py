# https://programmers.co.kr/learn/courses/30/lessons/42627


def solution(jobs):
    import heapq

    cnt = len(jobs)
    current = time = answer = 0
    heap = []

    jobs.sort(key=lambda e: e[0])
    while jobs or heap:
        while jobs and jobs[0][0] == current:   # 요청시간이 현재 시간과 같을 경우 힙에 push
            s, t = jobs.pop(0)
            heapq.heappush(heap, (t, s))

        if time > 0:
            time -= 1

        if time == 0:       # 현재 실행중인 작업이 없을 경우
            if heap:        # heap이 비어있지 않을 경우
                t, s = heapq.heappop(heap)
                time = t
                answer += (current - s) + t

        current += 1

    return answer // cnt


print(solution(eval(input())))





