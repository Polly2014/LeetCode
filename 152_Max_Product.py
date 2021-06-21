# -*- coding: utf-8 -*-
# @Author: polly
# @Date:   2021-06-21 22:29:34
# @Last Modified by:   polly
# @Last Modified time: 2021-06-21 23:03:42

# 最大乘积子序列
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp_max, dp_min = [0] * n, [0] * n
        for i in range(n):
            if i == 0:
                dp_max[i] = dp_min[i] = nums[i]
            else:
                choices = (nums[i], nums[i] * dp_min[i - 1], nums[i] * dp_max[i - 1])
                dp_max[i], dp_min[i] = max(choices), min(choices)
        return max(dp_max)


if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct(nums=[2, 3, -2, 4]))
