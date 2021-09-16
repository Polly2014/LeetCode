# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-17 00:20:26
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-17 00:33:30
from pysnooper import snoop


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = [None] * 26
        self.isEnd = False

    @snoop()
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    @snoop()
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                return False
            node = node.children[ch]
        return node and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        for ch in prefix:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                return False
        return True if node else False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
if __name__ == '__main__':
    obj = Trie()
    obj.insert('apple')
    print(obj.search('apple'))
