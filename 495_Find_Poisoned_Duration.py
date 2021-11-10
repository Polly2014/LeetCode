# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-10 21:37:30
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-10 21:38:24
from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        for i in range(len(timeSeries) - 1):
            ans += min(duration, timeSeries[i + 1] - timeSeries[i])
        ans += duration
        return ans
