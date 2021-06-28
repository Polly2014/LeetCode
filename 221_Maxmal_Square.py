# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-06-28 22:32:04
# @Last Modified by:   Polly
# @Last Modified time: 2021-06-28 23:15:41
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 获取宽高m,n
        m, n = len(matrix), len(matrix[0])
        # 定义DP数组，dp[i][j]表示以i为最后一行，j为最后一列的矩阵的边长（i,j在最大矩阵中）
        dp = [[0] * n for _ in range(m)]
        # 初始化第一列和第一行
        for i in range(m):
            dp[i][0] = 1 if matrix[i][0] == '1' else 0
        for j in range(n):
            dp[0][j] = 1 if matrix[0][j] == '1' else 0

        # 求解整个DP矩阵
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
        return max([max(d) for d in dp])**2


if __name__ == '__main__':
    s = Solution()
    print(s.maximalSquare([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
