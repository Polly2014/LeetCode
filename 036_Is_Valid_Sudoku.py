# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-17 15:26:01
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-17 15:33:58
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[0] * 10 for _ in range(9)]
        col = [[0] * 10 for _ in range(9)]
        box = [[0] * 10 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                # 检测单元格是否为非数组
                if board[i][j] == '.':
                    continue
                # 得到当前单元格数字
                curNumber = ord(board[i][j]) - ord('0')
                # 检测对应行
                if row[i][curNumber]:
                    return False
                # 检测对应列
                if col[j][curNumber]:
                    return False
                # 检测对应box
                if box[j // 3 + (i // 3) * 3][curNumber]:
                    return False

                # 如果都没出现过，则更新上去
                row[i][curNumber] = 1
                col[j][curNumber] = 1
                box[j // 3 + (i // 3) * 3][curNumber] = 1
        return True
