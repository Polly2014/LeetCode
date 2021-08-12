# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-11 20:24:46
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-11 20:47:26
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

    # def mySqrt(self, x: int) -> int:
    #     if x == 0:
    #         return 0

    #     C, x0 = float(x), float(x)
    #     while True:
    #         xi = 0.5 * (x0 + C / x0)
    #         if abs(x0 - xi) < 1e-7:
    #             break
    #         x0 = xi

    #     return int(x0)


if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(0))
