# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-10 16:44:39
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-10 16:44:49

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(list(s.split())[::-1])
