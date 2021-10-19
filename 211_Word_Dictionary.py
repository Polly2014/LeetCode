# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-19 10:36:00
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-19 23:27:54
from collections import defaultdict
from queue import deque
class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        cur = self.trie
        for c in word:
            if c not in self.trie:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = {}

    def search(self, word: str) -> bool:
        word += '#'
        Q = deque([(0, self.trie)])
        while Q:
            idx, cur = Q.popleft()
            if idx == len(word):
                return True
            if word[idx] == '.':
                for nxt in cur.values():
                    Q.append((idx + 1, nxt))
            elif word[idx] in cur:
                Q.append((idx + 1, cur[word[idx]]))
        return False

        pass

        # Your WordDictionary object will be instantiated and called as such:
        # obj = WordDictionary()
        # obj.addWord(word)
        # param_2 = obj.search(word)
if __name__ == '__main__':
    s = WordDictionary()
    s.addWord('hello')
    print(s.search('hel.o'))
    print(s.trie)
