# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-09 21:15:27
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-09 21:45:48
from typing import List
from sortedcontainers import SortedSet

class SummaryRanges:

    def __init__(self):
        self.mask = [False] * 10001

    def addNum(self, val: int) -> None:
        self.mask[val] = True

    def getIntervals(self) -> List[List[int]]:
        ans = []
        start, end = -1, -1
        for i in range(10001):
            if self.mask[i]:
                if start == -1:
                    start = i
                    end = i
                else:
                    end = i
            else:
                if start != -1:
                    ans.append([start, end])
                    start, end = -1, -1
        if start != -1:
            ans.append([start, end])
        return ans

        # Your SummaryRanges object will be instantiated and called as such:
        # obj = SummaryRanges()
        # obj.addNum(val)
        # param_2 = obj.getIntervals()
