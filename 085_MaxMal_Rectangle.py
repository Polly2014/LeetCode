# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-06-28 23:59:48
# @Last Modified by:   Polly
# @Last Modified time: 2021-07-03 16:50:50
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])

        heights = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        dp = [[[0] * (m + 1) for _ in range(n + 1)]for _ in range(m + 1)]
        ans = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '0':
                    continue
                heights[i][j] = heights[i - 1][j] + 1
                for k in range(1, heights[i][j] + 1):
                    dp[i][j][k] = dp[i][j - 1][k] + k
                    ans = max(ans, dp[i][j][k])
        return ans
    '''
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def compute(x):
            return x[0] * x[1]
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        ans = [0, 0]
        m, n = len(matrix), len(matrix[0])
        # 定义DP数组dp[i][j][2]
        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]
        # 初始化
        dp[0][0] = [1, 1] if matrix[0][0] == '1' else [0, 0]
        ans = dp[0][0] if compute(dp[0][0]) > compute(ans) else ans
        for i in range(1, m):
            if matrix[i][0] == '1':
                dp[i][0] = [1, dp[i - 1][0][1] + 1]
                ans = dp[i][0] if compute(dp[i][0]) > compute(ans) else ans
        for j in range(1, n):
            if matrix[0][j] == '1':
                dp[0][j] = [dp[0][j - 1][0] + 1, 1]
                ans = dp[0][j] if compute(dp[0][j]) > compute(ans) else ans
        # 遍历更新DP数组
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    up = dp[i - 1][j]
                    left = dp[i][j - 1]
                    if matrix[i - 1][j - 1] == '0':
                        dp[i][j] = [max(up[0], 1), up[1] + 1] if compute(up) > compute(left) else [left[0] + 1, max(left[1], 1)]
                    else:
                        dp[i][j] = [min(left[0], dp[i - 1][j - 1][0]) + 1, min(up[1], dp[i - 1][j - 1][1]) + 1]
                        if compute(left) + 1 > compute(dp[i][j]):
                            dp[i][j] = [left[0] + 1, 1]
                        if compute(up) + 1 > compute(dp[i][j]):
                            dp[i][j] = [1, up[1] + 1]
                ans = dp[i][j] if compute(dp[i][j]) > compute(ans) else ans
        return compute(ans)
    '''


if __name__ == '__main__':
    s = Solution()
    # print(s.maximalRectangle([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
    print(s.maximalRectangle([["0", "0", "0", "0", "0", "0", "1"], ["0", "0", "0", "0", "1", "1", "1"],
                              ["1", "1", "1", "1", "1", "1", "1"], ["0", "0", "0", "1", "1", "1", "1"]]))
