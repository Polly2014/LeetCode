# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-14 23:32:54
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-15 17:27:10
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans,path = [],[]
        def BackTracking(s, startIndex):
            if startIndex==len(s):
                if is_valid(path):
                    ans.append(path[:])
                return
            for i in range(startIndex, len(s)):
                pass
