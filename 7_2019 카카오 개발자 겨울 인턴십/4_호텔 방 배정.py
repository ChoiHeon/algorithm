# https://programmers.co.kr/learn/courses/30/lessons/64063


"""
* union find 알고리즘으로 해결 불가
  - 서브 트리의 루트: 해당 인덱스가 가리키는 방에 들어가고자 할 때 실제로 들어가게 되는 방의 번호
  - find 함수에서 스택 오버플로우 발생 (recursion error)(runtime error)
  - 확실하지 않음
  - parent를 list대신 dictionary로 구현 가능

"""


def solution(k, room_number):
    import sys
    sys.setrecursionlimit(10 ** 8)
    answer = []
    d = dict()

    def find(x):
        if x not in d.keys():
            answer.append(x)
            d[x] = x
            return x
        d[x] = find(d[x]+1)
        return d[x]

    for n in room_number:
        find(n)

    return answer


print(solution(eval(input()), eval(input())))
