# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-30 21:27:51
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-30 21:45:56
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        overlapWidth = min(ax2, bx2) - max(ax1, bx1)
        overlapHeight = min(ay2, by2) - max(ay1, by1)
        overlapArea = max(overlapWidth, 0) * max(overlapHeight, 0)
        return area1 + area2 - overlapArea


if __name__ == '__main__':
    s = Solution()
    print(s.computeArea(ax1=0, ay1=0, ax2=0, ay2=0, bx1=-1, by1=-1, bx2=1, by2=1))
