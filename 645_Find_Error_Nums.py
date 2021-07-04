# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-07-04 21:20:28
# @Last Modified by:   Polly
# @Last Modified time: 2021-07-04 21:45:16
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        '''
        哈希
        '''
        n, repeat, loss = len(nums), 0, 0
        ans = [0] * n
        for i in range(n):
            ans[nums[i] - 1] += 1
        for i in range(n):
            if ans[i] == 0:
                loss = i + 1
            if ans[i] == 2:
                repeat = i + 1
        return [repeat, loss]

    def findErrorNums(self, nums: List[int]) -> List[int]:
        '''
        # 好似鸡兔同笼
        1. sum(nums) - sum(set(nums)) = 重复的数字
        2. (1 + len(nums)) * len(nums) // 2 - sum(set(nums)) = 丢失的数字
        '''
        S = sum(set(nums))  # 去重，加和（此时相较于不丢失，加和少了那个丢失的数的值）
        return [sum(nums) - S, len(nums) * (len(nums) + 1) // 2 - S]


if __name__ == '__main__':
    s = Solution()
    print(s.findErrorNums([3, 2, 3, 4, 6, 5]))
