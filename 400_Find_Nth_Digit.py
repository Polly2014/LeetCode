# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-15 22:23:49
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-15 23:07:48
class Solution:
    def findNthDigit(self, n: int) -> int:
        # 判断target是几位数，用digit表示
        digits, base = 1, 9
        while n - digits * base > 0:
            n -= digits * base
            digits += 1
            base *= 10
        print(n, digits, base)
        i, j = divmod(n, digits)
        if j == 0:
            return int(str(10**(digits - 1) + i - 1)[-1])
        else:
            return int(str(10**(digits - 1) + i)[j - 1])


if __name__ == '__main__':
    s = Solution()
    print(s.findNthDigit(30))
