# -*- coding: utf-8 -*-
# @Author: polly
# @Date:   2021-06-23 23:17:44
# @Last Modified by:   polly
# @Last Modified time: 2021-06-23 23:23:04
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp_price = [0] * n
        if n < 2:
            return max(nums)
        dp_price[0] = nums[0]
        dp_price[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp_price[i] = max(dp_price[i - 2] + nums[i], dp_price[i - 1])
        return dp_price[n - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.rob([2, 7, 9, 3, 1]))
