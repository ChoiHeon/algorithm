"""
문자열 검색에 사용
시간 복잡도: O(m), m=문자열 최대 길이
"""


class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}      # key : value = character : Node


class Trie:
    def __init__(self):
        self.head = Node(key=None)  # key = None, data = None

    def insert_string(self, string):
        cursor = self.head
        for c in string:
            if c not in cursor.children.keys():
                cursor.children[c] = Node(key=c)
            cursor = cursor.children[c]
        cursor.data = string

    def search(self, string):
        cursor = self.head
        for c in string:
            if c not in cursor.children.keys():
                return False
            cursor = cursor.children[c]
        return cursor.data is not None

    def start_with(self, prefix):
        cursor = self.head
        for c in prefix:
            if c in cursor.children.keys():
                cursor = cursor.children[c]
            else:
                return []

        ret = []
        sub_trie = [cursor]
        while sub_trie:
            node = sub_trie.pop()
            if node.data is not None:
                ret.append(node.data)
            sub_trie += node.children.values()
        return ret


# Test Code
trie = Trie()
trie.insert_string("hello")
trie.insert_string("hi")
print(trie.start_with("h"))