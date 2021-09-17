# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-17 11:25:52
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-17 12:02:12
from typing import List
from collections import defaultdict


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = ''
        self.isEnd = False

    def insert(self, word):
        node = self
        for c in word:
            node = node.children[c]
        node.word = word
        node.isEnd = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 构建字典树
        trie = Trie()
        for word in words:
            trie.insert(word)

        # DFS搜索
        def DFS(node, x, y):
            # 获取当前字符
            ch = board[x][y]

            # 剪枝，定义异常中止条件（即未找到，且不可能再找到）
            if ch not in node.children:
                return

            # 判断是否正常中止条件（即找到）
            node = node.children[ch]
            if node.isEnd:
                ans.add(node.word)

            # 开始递归回溯逻辑
            board[x][y] = '#'
            for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= xx < m and 0 <= yy < n:
                    DFS(node, xx, yy)
            board[x][y] = ch

        # 定义变量
        ans = set()
        m, n = len(board), len(board[0])

        # 遍历board，开始深度搜索
        for i in range(m):
            for j in range(n):
                DFS(trie, i, j)

        # 将结果转为列表
        return list(ans)
