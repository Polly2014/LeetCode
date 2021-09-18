# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-18 18:22:09
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-18 21:28:04
from typing import List
from pysnooper import snoop


class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        @snoop()
        def BackTracking(path, startIndex):
            ans.append(path[:])
            for i in range(startIndex, n):
                if i > startIndex and nums[i] == nums[i - 1]:
                    continue
                BackTracking(path + [nums[i]], i + 1)
        nums.sort()
        BackTracking([], 0)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([1, 2, 2]))
