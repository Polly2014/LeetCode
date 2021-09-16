# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-16 00:03:44
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-16 00:11:11
from typing import List
from pysnooper import snoop
class Solution:
    @snoop()
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0]*n
        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                idx_stack = stack.pop()
                ans[idx_stack] = i-idx_stack
            stack.append(i)
        return ans
if __name__=='__main__':
    s = Solution()
    print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))