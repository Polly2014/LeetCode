# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-05 21:14:02
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-05 21:24:08
from typing import List
from collections import defaultdict


class Solution:
        # 方法一：DP数组，长度为i的数组的最长等差子序列
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if arr[i] - arr[j] == difference:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    # 方法二：DP数组，以i结尾的数组的最长等差子序列（HashMap的DP）
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for v in arr:
            dp[v] = dp[v - difference] + 1
        return max(dp.values())


if __name__ == '__main__':
    s = Solution()
    s.longestSubsequence([3, 4, -3, -2, -4], -5)
