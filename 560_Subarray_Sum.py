# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-12 16:08:45
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-12 21:39:30
from typing import List
import pysnooper


class Solution:
    @pysnooper.snoop()
    def subarraySum(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # counter = dict()
        # prefix, ans = 0, 0
        # for num in nums:
        #     prefix += num
        #     if prefix == k:
        #         ans += 1
        #     ans += counter.get(prefix - k, 0)
        #     counter[prefix] = counter.get(prefix, 0) + 1
        # return ans

        # 更清爽
        n = len(nums)
        counter = dict()
        prefix, ans = 0, 0
        counter[0] = 1
        for num in nums:
            prefix += num
            ans += counter.get(prefix - k, 0)
            counter[prefix] = counter.get(prefix, 0) + 1
        return ans

if __name__=='__main__':
    s = Solution()
    print(s.subarraySum([1,2,3,3,3,4,5,6,7,8,1,2,3], 8))
