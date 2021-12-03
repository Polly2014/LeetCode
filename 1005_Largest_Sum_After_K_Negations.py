# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-12-03 22:27:47
# @Last Modified by:   Polly
# @Last Modified time: 2021-12-03 22:31:42
from typing import List
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        num_min = min(nums)
        for i in range(k):
            num_min = min(nums)
            nums[nums.index(num_min)] = -num_min
        return sum(nums)

if __name__=='__main__':
    s = Solution()
    print(s.largestSumAfterKNegations([3,-1,0,2],3))