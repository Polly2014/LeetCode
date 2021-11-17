# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-16 23:05:36
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-16 23:31:20
from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        x, y, a, b, s = inf, inf, -inf, -inf, 0
        cnts = Counter()
        for x_, y_, a_, b_ in rectangles:
            x, y, a, b = min(x, x_), min(y, y_), max(a, a_), max(b, b_)
            s += (a_ - x_) * (b_ - y_)
            cnts[(x_, y_)] += 1
            cnts[(a_, b_)] += 1
            cnts[(x_, b_)] += 1
            cnts[(a_, y_)] += 1
        if s != (a - x) * (b - y):
            return False
        ps = {(x, y), (x, b), (a, y), (a, b)}
        for p in ps:
            if cnts[p] != 1:
                return False
        for i, v in cnts.items():
            if v > 4 or (i not in ps and v % 2):
                return False
        return True
