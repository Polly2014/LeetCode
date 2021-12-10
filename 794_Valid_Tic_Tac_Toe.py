# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-12-09 21:49:04
# @Last Modified by:   polly
# @Last Modified time: 2021-12-09 23:58:13
from typing import List


class Solution:
    def win(self, board: List[str], p: str) -> bool:
        return any(board[i][0] == p and board[i][1] == p and board[i][2] == p or
                   board[0][i] == p and board[1][i] == p and board[2][i] == p for i in range(3)) or \
            board[0][0] == p and board[1][1] == p and board[2][2] == p or \
            board[0][2] == p and board[1][1] == p and board[2][0] == p

    def validTicTacToe(self, board: List[str]) -> bool:
        oCount = sum(row.count('O') for row in board)
        xCount = sum(row.count('X') for row in board)
        return not (oCount != xCount and oCount != xCount - 1 or
                    oCount != xCount and self.win(board, 'O') or
                    oCount != xCount - 1 and self.win(board, 'X'))

    def validTicTacToe(self, board: List[str]) -> bool:
        sumO = board[0].count('O') + board[1].count('O') + board[2].count('O')
        sumX = board[0].count('X') + board[1].count('X') + board[2].count('X')
        # 检测行

        def checkRow(s):
            if board[0][0] == s and board[0][1] == s and board[0][2] == s or board[1][0] == s and board[1][1] == s and board[1][2] == s or board[2][0] == s and board[2][1] == s and board[2][2] == s:
                return True
            return False
        # 检测列

        def checkCol(s):
            if board[0][0] == s and board[1][0] == s and board[2][0] == s or board[0][1] == s and board[1][1] == s and board[2][1] == s or board[0][2] == s and board[1][2] == s and board[2][2] == s:
                return True
            return False
        # 检测斜对角

        def checkDia(s):
            if board[0][0] == s and board[1][1] == s and board[2][2] == s or board[2][0] == s and board[1][1] == s and board[0][2] == s:
                return True
            return False
        # X的数量较小返回False
        if not (sumX == sumO or sumX - sumO == 1):
            return False
        else:
            # X玩家走的时候判断O玩家是否赢了
            if sumX > sumO:
                if checkRow('O') or checkCol('O') or checkDia('O'):
                    return False
            else:
                # O玩家走的时候判断X玩家是否赢了
                if checkRow('X') or checkCol('X') or checkDia('X'):
                    return False
        return True
