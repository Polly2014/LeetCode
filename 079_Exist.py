# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-02 23:47:30
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-17 16:22:39
from typing import List
from pysnooper import snoop


class Solution:
    # DFS｜回溯+未剪枝
    # def __init__(self):
    #     self.ans = False

    # def exist(self, board: List[List[str]], word: str) -> bool:

    #     @snoop()
    #     def DFS(x, y, startIndex):
    #         # 获得当前单词
    #         ch = board[x][y]
    #         # 判断异常中止条件（未找到，且无需再找）
    #         if word[startIndex] != ch:
    #             return
    #         # 找到
    #         if startIndex == k - 1:
    #             self.ans = True
    #             return
    #         # 搜索回溯
    #         board[x][y] = '#'
    #         for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
    #             if 0 <= xx < m and 0 <= yy < n:
    #                 DFS(xx, yy, startIndex + 1)
    #         board[x][y] = ch
    #     # 获取行数、列数、单词长度
    #     m, n, k = len(board), len(board[0]), len(word)
    #     # 遍历，以每个单元格作为起点进行搜索
    #     for i in range(m):
    #         for j in range(n):
    #             DFS(i, j, 0)
    #     return self.ans

    # DFS｜回溯+剪枝
    def exist(self, board: List[List[str]], word: str) -> bool:

        @snoop()
        def DFS(x, y, startIndex):
            # 获得当前单词
            ch = board[x][y]
            # 判断异常中止条件（未找到，且无需再找）
            if word[startIndex] != ch:
                return False
            # 找到
            if startIndex == k - 1:
                return True
            result = False
            # 搜索回溯
            board[x][y] = '#'
            for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= xx < m and 0 <= yy < n:
                    if DFS(xx, yy, startIndex + 1):
                        return True
            board[x][y] = ch
            return result
        # 获取行数、列数、单词长度
        m, n, k = len(board), len(board[0]), len(word)
        # 遍历，以每个单元格作为起点进行搜索
        for i in range(m):
            for j in range(n):
                if DFS(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], 'ABCCED'))
