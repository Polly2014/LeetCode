# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-21 14:55:54
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-21 15:04:13
from typing import List


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        n = len(s)
        ans = []

        def BackTracking(path, startIndex):
            if startIndex == n:
                ans.append(format_path(path))
                return
            for i in range(startIndex, n):
                curr_str = s[startIndex:i + 1]
                if curr_str.startswith('0') and curr_str[-1] == '0':
                    break
                path.append(curr_str)
                BackTracking(path, i + 1)
                path.pop()
