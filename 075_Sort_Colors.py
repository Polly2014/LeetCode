# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-30 22:20:57
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-30 22:44:54
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p, q = 0, n - 1
        i = 0
        while i <= q:
            while i <= q and nums[i] == 2:
                nums[i], nums[q] = nums[q], nums[i]
                q -= 1
            if nums[i] == 0:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
            i += 1
        return nums
