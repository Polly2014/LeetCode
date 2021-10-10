# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-10 15:59:06
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-10 16:08:45
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right + 1) // 2
            if mid * (mid + 1) <= 2 * n:
                left = mid
            else:
                right = mid - 1
        return left


if __name__ == '__main__':
    s = Solution()
    print(s.arrangeCoins(3))
