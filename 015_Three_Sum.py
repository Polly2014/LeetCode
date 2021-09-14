# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-06-27 19:08:38
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-14 10:28:07
from typing import List
from pysnooper import snoop


class Solution:
    @snoop()
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            left, right = i + 1, n - 1
            if nums[i] > 0:
                break
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left != right and nums[left] == nums[left + 1]:
                        left += 1
                    while left != right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-3]))
