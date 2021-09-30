# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-30 23:46:01
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-30 23:50:18
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp_left = [1] * n
        dp_right = [1] * n
        for i in range(1, n):
            dp_left[i] = dp_left[i - 1] * nums[i - 1]
        for j in range(n - 2, -1, -1):
            dp_right[j] = dp_right[j + 1] * nums[j + 1]
        return [dp_left[i] * dp_right[i] for i in range(n)]


if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))
