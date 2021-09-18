# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-18 18:00:57
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-18 18:13:23
from typing import List


class Solution:
    # 经典回溯
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        n = len(nums)

        def BackTracking(nums, path, startIndex):
            if startIndex == n:
                ans.append(path[:])
                return
            if path not in ans:
                ans.append(path[:])
            for i in range(startIndex, n):
                path.append(nums[i])
                BackTracking(nums, path, i + 1)
                path.pop()
        BackTracking(nums, [], 0)
        return ans

    # 回溯优化版
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def BackTracking(nums, path, startIndex):
            ans.append(path[:])
            for i in range(startIndex, n):
                path.append(nums[i])
                BackTracking(nums, path, i + 1)
                path.pop()
        BackTracking(nums, [], 0)
        return ans

    # DFS版
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def BackTracking(nums, path, startIndex):
            ans.append(path[:])
            for i in range(startIndex, n):
                BackTracking(nums, path + [nums[i]], i + 1)
        BackTracking(nums, [], 0)
        return ans

    # 库函数
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums) + 1):
            for tmp in itertools.combinations(nums, i):
                res.append(tmp)
        return res


if __name__ == '__main__':
    s = Solution()
    s.subsets([1, 2, 3])
