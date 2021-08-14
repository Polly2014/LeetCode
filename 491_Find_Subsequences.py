# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-12 23:05:13
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-13 01:48:11
from typing import List


class Solution:
    # def findSubsequences(self, nums: List[int]) -> List[List[int]]:
    #     n = len(nums)
    #     ans, sub_seq = [], []

    #     def BackTrack(nums, idx_start):
    #         if len(sub_seq) > 1 and sub_seq not in ans:
    #             ans.append(sub_seq[:])
    #         for i in range(idx_start, n):
    #             if not sub_seq or nums[i] >= sub_seq[-1]:
    #                 sub_seq.append(nums[i])
    #                 BackTrack(nums, i + 1)
    #                 sub_seq.pop()
    #     BackTrack(nums, 0)
    #     return ans
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans, sub_seq = [], []

        def BackTrack(idx_start, sub_seq):
            repeat = []
            if len(sub_seq) > 1:
                ans.append(sub_seq[:])
            for i in range(idx_start, n):
                if nums[i] in repeat:
                    continue
                if not sub_seq or nums[i] >= sub_seq[-1]:
                    repeat.append(nums[i])
                    sub_seq.append(nums[i])
                    BackTrack(i + 1, sub_seq)
                    sub_seq.pop()
        BackTrack(0, [])
        return ans
    # def findSubsequences(self, nums: List[int]) -> List[List[int]]:
    #     n = len(nums)
    #     res = []
    #     path = []

    #     def backtrack(nums, startIndex):
    #         repeat = []  # 这里使用数组来进行去重操作
    #         if len(path) > 1:
    #             res.append(path[:])  # 注意这里不要加return，要取树上的节点
    #         for i in range(startIndex, n):
    #             if nums[i] in repeat:
    #                 continue
    #             if path and nums[i] < path[-1]:
    #                 continue
    #             if not path or nums[i] >= path[-1]:
    #                 repeat.append(nums[i])  # 记录这个元素在本层用过了，本层后面不能再用了
    #                 path.append(nums[i])
    #                 backtrack(nums, i + 1)
    #             path.pop()
    #     backtrack(nums, 0)
    #     return res


if __name__ == '__main__':
    s = Solution()
    print(s.findSubsequences([4, 6, 7, 7]))
