# -*- coding: utf-8 -*-
# @Author: polly
# @Date:   2021-06-21 23:22:17
# @Last Modified by:   polly
# @Last Modified time: 2021-06-21 23:28:42
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp_max = [0] * n
        dp_max[0] = nums[0]
        for i in range(1, n):
            dp_max[i] = max(dp_max[i - 1] + nums[i], nums[i])
        return max(dp_max)
