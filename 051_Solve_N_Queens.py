# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-03 20:56:15
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-04 23:22:59
from typing import List


class Solution:
    '''
    # BT
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        chessboard = [['.'] * n for _ in range(n)]

        def backtracking(n, row, chessboard):
            if row == n:
                ans.append([''.join(row) for row in chessboard])
                return
            for col in range(n):
                # print("Valid Result: [row:{},col:{}] {}".format(row, col, isValid(row, col, chessboard, n)))
                if isValid(row, col, chessboard, n):
                    chessboard[row][col] = 'Q'
                    backtracking(n, row + 1, chessboard)
                    chessboard[row][col] = '.'

        def isValid(row, col, chessboard, n):
            # 检测列
            for i in range(row):
                if chessboard[i][col] == 'Q':
                    return False
            # 检测斜左上方
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if chessboard[i][j] == 'Q':
                    return False
                i, j = i - 1, j - 1
            # 检测斜右上方
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if chessboard[i][j] == 'Q':
                    return False
                i, j = i - 1, j + 1
            return True
        backtracking(n, 0, chessboard)
        return ans
    '''

    def solveNQueens(self, n: int) -> List[List[str]]:
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return
            for q in range(n):
                if not in queens and p - q not in xy_dif and p + q not in xy_sum:
                    DFS(queens + [q], xy_dif + [p - q], xy_sum + [p + q])
            result = []
            DFS([], [], [])
            return [['.' * i + 'Q' + '.' * (n - i - 1) for i in sol] for sol in result]


if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))
