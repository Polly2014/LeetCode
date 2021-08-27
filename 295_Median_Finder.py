# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-27 22:56:50
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-27 23:27:32
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queMin = []
        self.queMax = []

    def addNum(self, num: int) -> None:
        queMin_ = self.queMin
        queMax_ = self.queMax
        if not queMin_ or num <= -queMin_[0]:
            heapq.heappush(queMin_, -num)
            if len(queMax_) + 1 < len(queMin_):
                heapq.heappush(queMax_, -heapq.heappop(queMin_))
        else:
            heapq.heappush(queMax_, num)
            if len(queMax_) > len(queMin_):
                heapq.heappush(queMin_, -heapq.heappop(queMax_))

    def findMedian(self) -> float:
        queMin_ = self.queMin
        queMax_ = self.queMax
        if len(queMin_) > len(queMax_):
            return - queMin_[0]
        return (-queMin_[0] + queMax_[0]) / 2.

        # Your MedianFinder object will be instantiated and called as such:
        # obj = MedianFinder()
        # obj.addNum(num)
        # param_2 = obj.findMedian()
