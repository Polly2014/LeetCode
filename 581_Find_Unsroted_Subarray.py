# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-04 20:05:33
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-04 20:24:07
from typing import List
from pysnooper import snoop


class Solution:
    # 排序
    @snoop()
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        left, right = 0, len(nums) - 1
        while left < len(nums) and sorted_nums[left] == nums[left]:
            left += 1
        while right > -1 and sorted_nums[right] == nums[right]:
            right -= 1
        ans = right - left + 1
        return ans if ans > 0 else 0

    # 一波遍历，更新边界
    # 算法背后的思想是无序子数组中最小元素的正确位置可以决定左边界，最大元素的正确位置可以决定右边界
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maxn, right = float('-inf'), -1
        minn, left = float('inf'), -1
        for i in range(n):
            if nums[i] < maxn:
                right = i
            else:
                maxn = nums[i]

            if nums[n - i - 1] > minn:
                left = n - i - 1
            else:
                minn = nums[n - i - 1]
        return 0 if right == -1 else right - left + 1


if __name__ == '__main__':
    s = Solution()
    s.findUnsortedSubarray([1, 2, 3, 4])
