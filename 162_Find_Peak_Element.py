# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-15 23:13:04
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-15 23:27:52
from typing import List
from pysnooper import snoop

class Solution:
    @snoop()
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(-float('inf'))
        n = len(nums)
        l,r = 0, n-2
        while l<=r:
            mid = (l+r)>>1
            if nums[mid]<nums[mid+1]:
                l = mid+1
            else:
                r = mid-1
        return l
if __name__=='__main__':
    s = Solution()
    print(s.findPeakElement([1,2,1,3,5,6,4]))