# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-12 22:41:27
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-12 22:43:27
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, 0, -1):
            for j in range(i + 1, n + 1):
                dp[i][j] = min(k + max(dp[i][k - 1], dp[k + 1][j]) for k in range(i, j))
        return dp[1][n]
