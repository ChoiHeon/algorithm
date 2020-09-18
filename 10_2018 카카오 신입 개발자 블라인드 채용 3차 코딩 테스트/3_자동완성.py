# https://programmers.co.kr/learn/courses/30/lessons/17685

"""
* 사용한 알고리즘
  - Trie 구조

* 시간초과
    - 단어를 저장할 때 단어를 슬라이스하여 재귀함수에 넘길 경우, 시간초과가 발생하였음
"""


import sys
sys.setrecursionlimit(10**6)

class data:
    def __init__(self, depth):
        self.depth = depth
        self.word_count = 0
        self.children = dict()
        self.is_end = False

    def save(self, word, i, n):
        c = word[i]
        if c not in self.children:
            self.children[c] = data(self.depth+1)
        if i == n-1:
            self.children[c].is_end = True
            self.children[c].word_count += 1
        else:
            self.children[c].save(word, i+1, n)
        self.word_count += 1

    def search(self):
        ret = 0
        if self.word_count == 1:
            return self.depth
        if self.is_end:
            ret += self.depth
        for child in self.children.values():
            ret += child.search()
        return ret

def solution(words):
    root = data(0)
    for word in words:
        root.save(word, 0, len(word))
    return root.search()


print(solution(eval(input())))

"""
def save(self, s):
    if s[0] not in self.children:
        self.children[s[0]] = data(self.depth+1, 0)
    if len(s) == 1:
        self.children[s].is_end = True
        self.children[s].word_count += 1
    else:
        self.children[s[0]].save(s[1:])
    self.word_count += 1    
"""