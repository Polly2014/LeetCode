# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-04 10:48:41
# @Last Modified by:   polly
# @Last Modified time: 2021-11-04 11:14:19
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:
            mid = (left + right) >> 1
            square = mid**2
            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
