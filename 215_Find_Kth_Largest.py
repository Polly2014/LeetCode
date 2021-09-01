# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-01 23:34:26
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-01 23:49:43
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while True:
            idx = self.parition(nums, l, r)
            if idx == k - 1:
                return nums[idx]
            elif idx < k - 1:
                l = idx + 1
            else:
                r = idx - 1

    def parition(self, nums: List[int], l: int, r: int) -> int:
        pivot = nums[l]
        while l < r:
            while l < r and nums[r] <= pivot:
                r -= 1
            nums[l] = nums[r]
            while l < r and nums[l] >= pivot:
                l += 1
            nums[r] = nums[l]
        nums[l] = pivot
        return l
