# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-25 12:18:25
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-25 16:27:06
from typing import List
from pysnooper import snoop
from collections import defaultdict


class Solution:
    def __init__(self):
        self.ans = 0

    # 递归（带返回值）
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def DFS(currSum, startIndex):
            if startIndex == n:
                if currSum == target:
                    return 1
                return 0

            return DFS(currSum + nums[startIndex], startIndex + 1) + DFS(currSum - nums[startIndex], startIndex + 1)
        return DFS(0, 0)

    # 递归（不带返回值）
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def DFS(currSum, startIndex):
            if startIndex == n:
                if currSum == target:
                    self.ans += 1
                return

            DFS(currSum + nums[startIndex], startIndex + 1)
            DFS(currSum - nums[startIndex], startIndex + 1)
        DFS(0, 0)
        return self.ans

    # 递归+记忆化
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memory = defaultdict(int)

        def DFS(currSum, startIndex):
            if startIndex == n:
                if currSum == target:
                    return 1
                return 0
            if (currSum, startIndex) in memory:
                return memory[(currSum, startIndex)]

            memory[(currSum, startIndex)] = DFS(currSum + nums[startIndex], startIndex + 1) + \
                DFS(currSum - nums[startIndex], startIndex + 1)
            return memory[(currSum, startIndex)]
        return DFS(0, 0)


if __name__ == '__main__':
    s = Solution()
    # print(s.findTargetSumWays([11, 31, 37, 36, 43, 40, 50, 18, 10, 15, 10, 35, 43, 25, 41, 43, 6, 22, 38, 38], target=3))
    print(s.findTargetSumWays([1, 1, 1, 1, 1], target=3))
