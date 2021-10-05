# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-05 13:50:31
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-05 16:47:19
from typing import List
from pysnooper import snoop


class Solution:
        # 动态规划
    def canPartition(self, nums: List[int]) -> bool:
        # 总长度小于2，无法划分，直接返回
        n = len(nums)
        if n < 2:
            return False
        # 总和为奇数，无法划分，直接返回
        total = sum(nums)
        maxNum = max(nums)
        if total & 1:
            return False
        # 计算需要的目标值（总和的一半），当最大值大雨目标值，无法划分，直接返回
        target = total // 2
        if maxNum > target:
            return False
        # 定义DP数组，并初始化第一行
        dp = [[False] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        # 遍历更新DP数组
        for i in range(1, n):
            for j in range(1, target + 1):
                if nums[i] <= j:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
        for d in dp:
            print(d)
        return dp[n - 1][target]

    # 回溯
    def canPartition(self, nums: List[int]) -> bool:
        # 总长度小于2，无法划分，直接返回
        n = len(nums)
        if n < 2:
            return False
        # 总和为奇数，无法划分，直接返回
        total = sum(nums)
        maxNum = max(nums)
        if total & 1:
            return False
        # 计算需要的目标值（总和的一半），当最大值大雨目标值，无法划分，直接返回
        target = total // 2
        if maxNum > target:
            return False
        nums_sorted = sorted(nums, reverse=True)
        mem = {}

        @snoop()
        def BackTracking(remain, startIndex):
            if remain == 0:
                return True
            if startIndex == n or remain < 0:
                return False
            if startIndex in mem.keys():
                return mem[startIndex]
            for i in range(startIndex, n):
                if BackTracking(remain - nums_sorted[i], i + 1):
                    return True
            mem[startIndex] = False
            return False
        return BackTracking(target, 0)

    # 系统缓存
    # def canPartition(self, nums: List[int]) -> bool:
    #     import functools

    #     @functools.lru_cache(None)
    #     def subsearch(idx, sum1):
    #         if sum1 > total:
    #             return False
    #         elif sum1 == total:
    #             return True
    #         if idx == len(nums):
    #             return False
    #         else:
    #             return subsearch(idx + 1, sum1 + nums[idx]) or subsearch(idx + 1, sum1)

    #     if not nums:
    #         return True
    #     total = sum(nums)
    #     if total % 2 == 1:
    #         return False
    #     total //= 2
    #     nums.sort(reverse=True)
    #     return subsearch(0, 0)


if __name__ == '__main__':
    s = Solution()
    print(s.canPartition([1, 2, 3, 4, 5, 6, 7]))
