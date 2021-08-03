# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-03 20:56:15
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-03 22:41:51
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        chessboard = [['.'] * n for _ in range(n)]

        def backtracking(n, row, chessboard):
            if row == n:
                ans.append(chessboard)
                return
            for col in range(n):
                if isValid(row, col, chessboard, n):
                    chessboard[row][col] = 'Q'
                    backtracking(n, row + 1, chessboard)
                    chessboard[row][col] = '.'

        def isValid(row, col, chessboard, n):
            count = 0
            # 检测列
            if sum([chessboard[i][col] == 'Q' for i in range(row)]):
                return False
