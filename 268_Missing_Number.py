# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-06 15:05:07
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-06 15:09:21
from typing import List


class Solution:
    # Math
    def missingNumber(self, nums: List[int]) -> int:
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)

    # XOR
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        for i, num in enumerate(nums):
            xor ^= i ^ num
        return xor ^ len(nums)
