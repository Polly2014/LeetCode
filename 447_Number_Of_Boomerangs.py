# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-13 00:19:46
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-13 00:21:32
from typing import List
from collections import defaultdict


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for p in points:
            cnt = defaultdict(int)
            for q in points:
                dist = (p[0] - q[0])**2 + (p[1] - q[1])**2
                cnt[dist] += 1
            for v in cnt.values():
                ans += v * (v - 1)
        return ans
