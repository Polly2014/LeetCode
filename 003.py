# -*- coding: utf-8 -*-
# @Author: polly
# @Date:   2021-06-17 22:09:15
# @Last Modified by:   polly
# @Last Modified time: 2021-06-17 22:22:39

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = ''
        curr = ''
        for i in s:
            if i not in curr:
                curr += i
            else:
                record_dict[item]
