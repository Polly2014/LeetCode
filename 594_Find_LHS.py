# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-20 17:32:54
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-21 22:04:57
from typing import List
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return max([v + cnt[k + 1] for k, v in cnt.items() if k + 1 in cnt] + [0])
