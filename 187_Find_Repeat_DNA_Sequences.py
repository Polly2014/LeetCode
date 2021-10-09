# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-08 14:47:25
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-08 14:53:12
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        seen = set()
        ans = set()
        for i in range(0, n - 9):
            ss = s[i:i + 10]
            if ss in seen:
                ans.add(ss)
            else:
                seen.add(ss)
        return list(ans)
