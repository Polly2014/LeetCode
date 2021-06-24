# -*- coding: utf-8 -*-
# @Author: polly
# @Date:   2021-06-24 23:16:12
# @Last Modified by:   polly
# @Last Modified time: 2021-06-24 23:32:54
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        dp_profit = [0] * days
        min_price = prices[0]
        for day in range(1, days):
            min_price = min(min_price, prices[day])
            dp_profit[day] = max(dp_profit[day - 1], prices[day] - min_price)
        return dp_profit[days - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
