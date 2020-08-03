# https://programmers.co.kr/learn/courses/30/lessons/60060

"""
효울성 100% 통과를 하기 위해 trie 자료구조를 사용
query 를 Trie 에 저장할 경우 효율이 떨어지므로 (bfs 탐색을 해야 하므로)
word 를 저장

* query 의 길이
    - Trie 객체를 원소로 가지는 리스트를 생성
    - word 의 길이를 인덱스로 하는 Trie 객체에 삽입
    - query 의 길이를 인덱스로 하는 Trie 객체에서 해를 찾음

* 추가 가능 조건
    - query 의 중복이 가능
    - dict()를 사용하여 동일한 query 를 갖는 인덱스들을 저장
    - set()을 사용하여 query 의 중복을 제거
"""

from collections import deque


class Node:
    def __init__(self, key):
        self.key = key
        self.cnt = 0
        self.children = {}      # key : value = character : Node


class Trie:
    def __init__(self):
        self.head = Node(key=None)  # key = None, cnt = 0

    def insert_string(self, string):
        cursor = self.head
        for c in string:
            if c not in cursor.children.keys():
                cursor.children[c] = Node(key=c)
            cursor.cnt += 1
            cursor = cursor.children[c]
        cursor.cnt += 1

    def search(self, prefix):
        cursor = self.head
        for c in prefix:
            if c not in cursor.children.keys():
                return 0
            cursor = cursor.children[c]
        return cursor.cnt


def solution(words, queries):
    answer = []
    A = [Trie() for _ in range(10001)]
    B = [Trie() for _ in range(10001)]

    for word in words:
        A[len(word)].insert_string(word)
        B[len(word)].insert_string(word[::-1])

    for query in queries:
        flag = query[0] != '?'
        string = query if flag else query[::-1]
        prefix = string[:string.index('?')]
        answer.append(A[len(string)].search(prefix) if flag else B[len(string)].search(prefix))

    return answer


print(solution(["frodo", "frond", "frost", "frozen", "frame", "kakao"], ["fro??", "?????"]))
