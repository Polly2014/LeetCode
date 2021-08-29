# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-29 21:41:37
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-29 21:42:06
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
