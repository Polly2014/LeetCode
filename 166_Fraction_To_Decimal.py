# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-03 18:10:16
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-03 19:34:15
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # 对于能整除的，直接返回
        if numerator % denominator == 0:
            return str(numerator // denominator)
        # 判断符号
        sign = '-' if numerator * denominator < 0 else ''
        # 将分子分母均转换为正数
        numerator, denominator = abs(numerator), abs(denominator)
        # 处理整数部分
        if numerator > denominator:
            ans = str(numerator // denominator) + '.'
            numerator %= denominator
        else:
            ans = '0.'
        # 处理小数部分
        numerator *= 10
        remainder = {}
        while numerator:
            q, numerator = divmod(numerator, denominator)
            if (q, numerator) in remainder:
                ans = ans[:remainder[q, numerator]] + '(' + ans[remainder[q, numerator]:] + ')'
                return sign + ans
            remainder[q, numerator] = len(ans)
            ans += str(q)
            numerator *= 10
        return sign + ans
