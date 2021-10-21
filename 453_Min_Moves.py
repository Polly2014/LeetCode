# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-20 21:38:59
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-21 17:00:55
from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # 使得n-1个元素加1，等价为使某个元素减1
    num_min = min(nums)
    return sum([num - num_min for num in nums])
