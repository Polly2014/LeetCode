# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-07 12:16:18
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-07 12:21:36
from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return min([op[0] for op in ops]+[m])*min([op[1] for op in ops]+[n])

if __name__=='__main__':
    s = Solution()
    print(s.maxCount(3,3,[[2,2],[3,3]]))