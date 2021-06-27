# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-06-25 23:35:55
# @Last Modified by:   Polly
# @Last Modified time: 2021-06-26 14:05:52
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # dp_profit[<天数>][<是否持有>][<交易（卖出）次数>]
        dp_profit = [[[0] * 3 for _ in range(2)] for _ in range(n)]
        for i in range(3):
            dp_profit[0][0][i], dp_profit[0][1][i] = 0, -prices[0]
        for i in range(1, n):
            for j in range(3):
                dp_profit[i][0][j] = max(dp_profit[i - 1][0][j], dp_profit[i - 1][0][j]
                                         if j == 0 else dp_profit[i - 1][1][j - 1] + prices[i])
                dp_profit[i][1][j] = max(dp_profit[i - 1][1][j], dp_profit[i - 1][0][j] - prices[i])
        return dp_profit[n - 1][0][2]


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
