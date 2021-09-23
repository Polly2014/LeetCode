# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-23 17:43:24
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-23 17:43:48
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n >= 3:
            n /= 3
        return n == 1
