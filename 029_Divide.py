# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-12 22:26:16
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-12 22:48:57
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 2 ** 31 and divisor == -1:
            return 2 ** 31 - 1
        a, b, res = abs(dividend), abs(divisor), 0
        for i in range(31, -1, -1):
        	# 2^i*b<=a   等价于 a/b = 2^i + (a-2^i*b)/b
            if a >= b << i:
                res += 1 << i
                a -= b << i
        return res if (dividend > 0) == (divisor > 0) else -res
