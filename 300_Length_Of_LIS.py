# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-06-28 21:58:54
# @Last Modified by:   Polly
# @Last Modified time: 2021-06-28 22:57:11
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i]数组含义：以长度i结尾的字符串，最长递增子序列
        dp = [1] * n
        # 初始化，一个字符时，最长递增子序列即为1
        # 考虑状态转移，第i个位置，会有前[0,i-1]的最长递增子序列共同决定
        for i in range(1, n):
            for j in range(i):
                dp[i] = max(dp[i], dp[j] + 1 if nums[i] > nums[j] else dp[i])
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
