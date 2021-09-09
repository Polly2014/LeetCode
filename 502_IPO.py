# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-08 21:56:16
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-08 22:15:17
from typing import List
import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital):
            return w + sum(sorted(profits, reverse=True)[:k])
        n = len(profits)

        capital_profit = [(capital[i], profits[i]) for i in range(n)]
        capital_profit.sort(key=lambda x: x[0])
        HQ = []
        i = 0
        for _ in range(k):
            while i < n and capital_profit[i][0] <= w:
                heapq.heappush(HQ, -capital_profit[i][1])
                i += 1
            if HQ:
                w -= heapq.heappop(HQ)
            else:
                break
        return w


if __name__ == '__main__':
    s = Solution()
    print(s.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))
