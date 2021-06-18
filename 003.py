# -*- coding: utf-8 -*-
# @Author: polly
# @Date:   2021-06-17 22:09:15
# @Last Modified by:   polly
# @Last Modified time: 2021-06-17 22:39:00

# Pythonic 滑得优雅
#  - 滑动窗口
#  - python index就OK

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        curr = ''
        for i in s:
            if i in curr:
                curr = curr[curr.index(i)+1:]
            curr += i
            if len(curr) > ans:
            	ans = len(curr)
        return ans
