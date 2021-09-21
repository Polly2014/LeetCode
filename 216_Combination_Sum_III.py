# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-21 14:01:56
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-21 14:34:40
from typing import List
from pysnooper import snoop


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def BackTracking(path, startNum):
            print('Path:{}, startNum:{}'.format(path, startNum))
            if startNum > n:
                return
            if len(path) == k:
                if sum(path) == n:
                    ans.append(path[:])
                return

            for i in range(startNum, 10):
                path.append(i)
                if len(path) <= k:
                    BackTracking(path, i + 1)
                path.pop()
        BackTracking([], 1)
        return ans


if __name__ == '__main__':
    s = Solution()
    s.combinationSum3(3, 7)
