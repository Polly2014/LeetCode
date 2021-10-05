# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-06 00:28:57
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-06 00:29:07
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        n = len(nums)
        return nums[-1] if n < 3 else nums[-3]
