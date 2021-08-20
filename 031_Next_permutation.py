# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-20 22:53:07
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-20 23:29:14
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        firstIndex, secondIndex = -1, -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                firstIndex = i
                break
        if firstIndex == -1:
            nums[:] = nums[::-1]
        else:
            for j in range(n - 1, firstIndex, -1):
                if nums[j] > nums[firstIndex]:
                    secondIndex = j
                    break
            nums[firstIndex], nums[secondIndex] = nums[secondIndex], nums[firstIndex]
            nums[firstIndex + 1:] = nums[firstIndex + 1:][::-1]


if __name__ == '__main__':
    s = Solution()
    s.nextPermutation([3, 2, 1])
