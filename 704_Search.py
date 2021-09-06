# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-06 23:03:46
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-06 23:25:32
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            print('left: {}, right: {}, mid: {}'.format(left, right, mid))
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search([-1, 0, 3, 5, 9, 12], 0))
