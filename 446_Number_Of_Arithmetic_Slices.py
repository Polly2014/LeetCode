# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-11 00:21:59
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-12 10:23:46
from typing import List
from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n, ans = len(nums), 0
        dp = [defaultdict(int) for _ in range(n)]
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1
                ans += dp[j][diff]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfArithmeticSlices([2, 4, 6, 8, 10]))
