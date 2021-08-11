# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-11 20:24:46
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-11 20:36:22
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while True:
            mid = (l + r) // 2
            if mid**2 <= x and (mid + 1)**2 > x:
                return mid
            elif mid**2 < x:
                l = mid + 1
            else:
                r = mid - 1


if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(0))
