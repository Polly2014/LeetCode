# -*- coding: utf-8 -*-
# @Author: polly
# @Date:   2021-06-24 23:44:09
# @Last Modified by:   polly
# @Last Modified time: 2021-06-24 23:58:34
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        dp_profit = [[0] * 2 for _ in range(days)]
        dp_profit[0] = [0, -prices[0]]
        # dp[i][0]表示第i天不持有股票, dp[i][1]表示第i天持有股票
        for day in range(1, days):
            dp_profit[day][0] = max(dp_profit[day - 1][0], dp_profit[day - 1][1] + prices[day])
            dp_profit[day][1] = max(dp_profit[day - 1][1], dp_profit[day - 1][0] - prices[day])
        return dp_profit[days - 1][0]
