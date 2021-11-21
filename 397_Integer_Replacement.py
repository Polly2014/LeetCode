# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-19 22:07:33
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-19 22:14:02
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return 1 + self.integerReplacement(n // 2)
        return 2 + min(self.integerReplacement(n // 2）, self.integerReplacement(n // 2 + 1)))
