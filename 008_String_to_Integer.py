# -*- coding: utf-8 -*-
# @Author: polly
# @Date:   2021-06-19 15:32:13
# @Last Modified by:   polly
# @Last Modified time: 2021-06-19 15:32:24

class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)
