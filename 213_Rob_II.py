# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-06-27 22:46:29
# @Last Modified by:   Polly
# @Last Modified time: 2021-06-27 22:57:06
from typing import List


class Solution:
    def rob_sublist(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(n)]
        dp[0] = [0, nums[0]]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])
            dp[i][1] = dp[i - 1][0] + nums[i]
        return max(dp[n - 1])

    def rob(self, nums: List[int]) -> int:
        if k := len(nums) < 2:
            return max(nums)
        ans = [0, 0]
        ans[0] = self.rob_sublist(nums[1:])
        ans[1] = self.rob_sublist(nums[:-1])
        return max(ans)


if __name__ == '__main__':
    s = Solution()
    print(s.rob([1, 2, 3, 1]))
