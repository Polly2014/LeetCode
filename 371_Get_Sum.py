# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-26 10:45:42
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-26 22:30:09
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0x100000000
        # 整形最大值（除去符号位）
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1
        while b:
            # 计算进位
            carry = (a & b) << 1
            # 取余范围限制在[0, 2^32-1]范围内
            a = (a ^ b) % MASK
            b = carry % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)
        print(MIN_INT)

    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            sign = (a & b) << 1
            a = a ^ b
            b = sign
        return a|b


if __name__ == '__main__':
    s = Solution()
    print(s.getSum(-1, 1))
