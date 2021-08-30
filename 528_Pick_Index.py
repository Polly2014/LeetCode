# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-30 22:08:55
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-30 22:15:24
from typing import List
from itertools import accumulate
import random
from bisect import bisect_left
class Solution:

    def __init__(self, w: List[int]):
        self.pre = list(accumulate(w))
        self.total = sum(w)

    def pickIndex(self) -> int:
        x = random.randint(1, self.total)
        return bisect_left(self.pre, x)

        # Your Solution object will be instantiated and called as such:
        # obj = Solution(w)
        # param_1 = obj.pickIndex()
