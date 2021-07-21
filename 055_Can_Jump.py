# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-07-21 23:16:42
# @Last Modified by:   Polly
# @Last Modified time: 2021-07-21 23:22:52
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(1, n):
            for j in range(i):
                if dp[j] == True and nums[j] >= i - j:
                    dp[i] = True
        return dp[n - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.canJump([2, 1, 1, 0, 4]))
