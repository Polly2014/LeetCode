# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-03 10:58:53
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-03 12:21:55
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def backtracking(n, k, start_idx):
            if len(path) == k:
                print(path)
                ans.append(path[:])
                return
            for i in range(start_idx, n + 1):
                path.append(i)
                backtracking(n, k, i + 1)
                path.pop(-1)
        backtracking(n, k, 1)
        return ans


if __name__ == '__main__':
    s = Solution()
    s.combine(4, 2)
