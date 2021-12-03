# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-12-01 23:26:47
# @Last Modified by:   Polly
# @Last Modified time: 2021-12-01 23:30:18
class Solution:
    def maxPower(self, s: str) -> int:
        n = len(s)
        base,cnt = s[0],1
        ans = 1
        for i in range(1,n):
            if s[i]==base:
                cnt +=1
                ans = max(ans, cnt)
            else:
                base,cnt = s[i],1
        return ans
