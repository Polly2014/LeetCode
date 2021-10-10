# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-09 21:15:27
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-10 11:43:38
from typing import List
from sortedcontainers import SortedSet


class SummaryRanges:
    # 并查集
    def __init__(self):
        self.father = [-1 for i in range(10001)]

    def addNum(self, val: int) -> None:
        if self.father[val] == -1:
            self.father[val] = val
            self.union(val, val + 1)
            self.union(val - 1, val)

    def find(self, x):
        if self.father[x] != x:
            self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, x, y):
        if 0 <= x <= 10000 and self.father[x] != -1 and self.father[y] != -1:
            father_x = self.find(x)
            father_y = self.find(y)
            if father_x != father_y:
                self.father[father_x] = father_y

    def getIntervals(self) -> List[List[int]]:
        ans = []
        i = 0
        while i < 10001:
            if self.father[i] != -1:
                start = i
                end = self.find(i)
                ans.append([start, end])
                i = end + 1
            else:
                i += 1
        return ans

    '''经典模拟
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
    '''
    # Your SummaryRanges object will be instantiated and called as such:
    # obj = SummaryRanges()
    # obj.addNum(val)
    # param_2 = obj.getIntervals()
