# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-14 21:22:14
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-14 21:29:45
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right + 1) >> 1
            if arr[mid - 1] < arr[mid]:
                left = mid
            else:
                right = mid - 1
        return left


if __name__ == '__main__':
    s = Solution()
    print(s.peakIndexInMountainArray([1, 3, 5, 4, 2]))
