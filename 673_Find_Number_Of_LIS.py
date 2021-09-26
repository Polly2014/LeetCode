# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-20 14:03:46
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-25 17:05:41
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[k]: 以位置k结尾的数组最长递增子序列长度
        dp = [1] * n
        # cnt[k]: 以位置k结尾的数组最长递增子序列个数
        cnt = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                        # 更新cnt
                    if dp[j] + 1 > dp[i]:
                        # dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]
                    # 更新dp
                    dp[i] = max(dp[i], dp[j] + 1)
                print('i={},j={},cnt={}'.format(i, j, cnt))
        print(nums)
        print(dp)
        print(cnt)
        return sum([cnt[i] for i in range(n) if dp[i] == max(dp)])

    # def findNumberOfLIS(self, nums: List[int]) -> int:
    #     size = len(nums)
    #     if size <= 1:
    #         return size

    #     dp = [1 for i in range(size)]
    #     count = [1 for i in range(size)]

    #     maxCount = 0
    #     for i in range(1, size):
    #         for j in range(i):
    #             if nums[i] > nums[j]:
    #                 if dp[j] + 1 > dp[i]:
    #                     dp[i] = dp[j] + 1
    #                     count[i] = count[j]
    #                 elif dp[j] + 1 == dp[i]:
    #                     count[i] += count[j]
    #             if dp[i] > maxCount:
    #                 maxCount = dp[i]
    #     result = 0
    #     for i in range(size):
    #         if maxCount == dp[i]:
    #             result += count[i]
    #     print(nums)
    #     print(dp)
    #     print(count)
    #     return result


if __name__ == '__main__':
    s = Solution()
    s.findNumberOfLIS([1, 3, 5, 4, 7])
