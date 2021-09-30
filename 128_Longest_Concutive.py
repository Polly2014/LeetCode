# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-30 23:35:53
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-30 23:39:02
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                dp[i] = dp[i - 1] + 1
            elif nums[i] == nums[i - 1]:
                dp[i] = dp[i - 1]
        print(dp)
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    s.longestConsecutive([1, 2, 0, 1])
