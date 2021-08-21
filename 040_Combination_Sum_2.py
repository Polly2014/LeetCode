# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-21 23:08:56
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-21 23:38:27
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        path = []
        used = [0] * n

        def BackTracking(pathSum, startIndex, used):
            if startIndex > n or pathSum > target:
                return
            if pathSum == target:
                ans.append(path[:])
                return
            for i in range(startIndex, n):
                # 剪枝
                if pathSum + candidates[i] > target:
                    return
                if i > startIndex and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                BackTracking(pathSum + candidates[i], i + 1, used)
                path.pop()

        candidates.sort()
        BackTracking(0, 0, used)
        print(ans)


if __name__ == '__main__':
    s = Solution()
    s.combinationSum2([2, 5, 2, 1, 2], 5)
