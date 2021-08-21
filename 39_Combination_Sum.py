# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-21 21:52:05
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-21 23:04:35
from typing import List


class Solution:
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     n = len(candidates)
    #     ans = []

    #     def DFS(idx, combine, res):
    #         if idx >= n or res >= target:
    #             if res == target:
    #                 ans.append(combine[:])
    #             return
    #         combine.append(candidates[idx])
    #         DFS(idx, combine, res + candidates[idx])
    #         combine.pop()
    #         DFS(idx + 1, combine, res)
    #     DFS(0, [], 0)
    #     print(ans)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        path = []

        def BackTracking(candidates, target, sum_path, startIndex):
            if sum_path > target:
                return
            if sum_path == target:
                ans.append(path[:])
                return
            for i in range(startIndex, n):
                if sum_path + candidates[i] > target:
                    return
                sum_path += candidates[i]
                path.append(candidates[i])
                BackTracking(candidates, target, sum_path, i)
                sum_path -= candidates[i]
                path.pop()
        BackTracking(candidates, target, 0, 0)
        print(ans)


if __name__ == '__main__':
    s = Solution()
    s.combinationSum([2, 3, 6, 7], 7)
