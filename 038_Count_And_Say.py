# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-15 20:26:51
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-15 20:36:49
class Solution:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        for _ in range(n - 1):
            new_ans = ''
            l, r = 0, 0
            while l < len(ans):
                while r < len(ans) and ans[l] == ans[r]:
                    r += 1
                new_ans += str(r - l) + ans[l]
                l = r
            ans = new_ans
        return ans
