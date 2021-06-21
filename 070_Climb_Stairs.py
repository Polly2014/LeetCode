# -*- coding: utf-8 -*-
# @Author: polly
# @Date:   2021-06-21 23:09:52
# @Last Modified by:   polly
# @Last Modified time: 2021-06-21 23:16:46

class Solution:
    def climbStairs(self, n: int) -> int:
        dp_num = [0] * (n + 1)
        dp_num[0] = dp_num[1] = 1
        for i in range(2, n + 1):
            dp_num[i] = dp_num[i - 1] + dp_num[i - 2]
        return dp_num[n]
