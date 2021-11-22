# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-22 21:28:52
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-22 21:32:36
from typing import List
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.nums_origin = nums.copy()

    def reset(self) -> List[int]:
    	self.nums = self.nums_origin.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        random.shuffle(self.nums)
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
