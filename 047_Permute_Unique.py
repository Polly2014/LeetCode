# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-30 22:55:05
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-30 23:15:36
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        used = [False] * n

        def BackTracking(new_list):
            if len(new_list) == n:
                ans.append(new_list[:])
                return
            for i, num in enumerate(nums):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue
                    new_list.append(num)
                    used[i] = True
                    BackTracking(new_list)
                    new_list.pop()
                    used[i] = False
        BackTracking([])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1, 1, 2]))
