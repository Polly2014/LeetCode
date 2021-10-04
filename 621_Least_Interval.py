# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-04 18:16:00
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-04 18:18:00
from typing import List
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt_list = list(Counter(tasks).values())
        maxCnt = max(cnt_list)
        eleMaxCnt = cnt_list.count(maxCnt)
        return max(len(tasks), (maxCnt - 1) * (n + 1) + eleMaxCnt)
