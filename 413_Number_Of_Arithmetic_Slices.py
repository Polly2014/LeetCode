# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-10 12:37:27
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-10 12:41:33
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i - 1] + 1
        return sum(dp)


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfArithmeticSlices([1, 2, 3, 4]))
