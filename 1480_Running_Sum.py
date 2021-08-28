# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-28 22:00:33
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-28 22:02:27
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = dp[i - 1] + nums[i]
        return dp


if __name__ == '__main__':
    s = Solution()
    print(s.runningSum([1, 2, 3, 4]))
