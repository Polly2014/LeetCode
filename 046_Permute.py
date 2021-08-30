# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-30 22:21:42
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-30 22:31:38
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def BackTracking(new_list):
            if len(new_list) == n:
                ans.append(new_list[:])
                return
            for num in nums:
                if num not in new_list:
                    new_list.append(num)
                    BackTracking(new_list)
                    new_list.pop()
        BackTracking([])
        return ans


if __name__ == '__main__':
    s = Solution()
    s.permute([1, 2, 3])
