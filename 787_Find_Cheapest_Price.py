# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-24 20:44:57
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-24 21:40:46
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # DP数组定义 dp[t][i] 飞t次航班从src到达目的地i的最便宜价格
        # 则有状态转移:
        #  dp[t][i] = min(dsrc
        #  当t=0时，dp[0][src]=0, dp[0][j!=src]=inf
        dp = [[float('inf')] * n for _ in range(k + 2)]
        dp[0][src] = 0
        for t in range(1, k + 2):
            for j, i, cost in flights:
                dp[t][i] = min(dp[t][i], dp[t - 1][j] + cost)
        ans = min([dp[t][dst] for t in range(k + 2)])
        return -1 if ans == float('inf') else ans


if __name__ == '__main__':
    s = Solution()
    s.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1)
